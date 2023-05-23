import math
import os

import numpy as np
from torch import optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import torch.nn as nn
import torch
from torch.utils.tensorboard import SummaryWriter
from torch.optim import Optimizer

# 定义 transforms
transform = transforms.Compose(
    # 将数据格式转为Tensor(范围为(0-1))
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
)

root = r"H:\data\Cifar10"
cifar10_train = datasets.CIFAR10(root=r"H:\data\Cifar10", train=True, transform=transforms.ToTensor(), download=True)
cifar10_test = datasets.CIFAR10(root=r"H:\data\Cifar10", train=False, transform=transforms.ToTensor(), download=True)


# 自定义二维卷积层
class Conv2d(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0, padding_mode="zeros"):
        super(Conv2d, self).__init__()
        self.stride = stride
        self.padding = padding
        self.padding_mode = padding_mode
        # 张量化权重参数
        self.weight = nn.Parameter(torch.Tensor(out_channels, in_channels, kernel_size, kernel_size))
        # 张量化偏差参数
        self.bias = nn.Parameter(torch.Tensor(out_channels))
        # 初始化参数
        self.reset_parameters()

    def reset_parameters(self):
        # 使用K-mean均值初始化权重参数,以a为下界
        nn.init.kaiming_uniform_(self.weight, a=math.sqrt(5))
        # 初始化bias
        if self.bias is not None:
            # 计算fan_in值
            fan_in, _ = nn.init._calculate_fan_in_and_fan_out(self.weight)
            # 使用fan_in值计算bound
            bound = 1 / math.sqrt(fan_in)
            # 调用bound初始化bias
            nn.init.uniform_(self.bias, -bound, bound)

    # 定义前向计算方法
    def forward(self, x):
        # 如果输入的有padding值, 使用pad函数填充输入x值
        if self.padding > 0:
            if self.padding_mode == 'zeros':
                # 使用0值填充: 优点是简单直接,缺点是可能导致信息的丢失。适用于图像处理任务。
                x = torch.nn.functional.pad(x,
                                            (self.padding, self.padding, self.padding, self.padding), mode='constant',
                                            value=0)
            elif self.padding_mode == 'reflect':
                # 使用反射填充:优点是可以保留更多信息,缺点是可能产生重复图案。适用于图像处理任务。
                x = torch.nn.functional.pad(x, (self.padding, self.padding, self.padding, self.padding), mode='reflect')
            elif self.padding_mode == 'replicate':
                # 使用复制填充：优点和reflect相似,缺点也相似。适用于图像处理任务
                x = torch.nn.functional.pad(x, (self.padding, self.padding, self.padding, self.padding),
                                            mode='replicate')
            elif self.padding_mode == 'circular':
                # 使用循环填充：将图像上下或左右两边缘的值循环填充。优点是可以最大限度保留信息,缺点是产生更多的重复图案。适用于图像处理任务。
                x = torch.nn.functional.pad(x, (self.padding, self.padding, self.padding, self.padding),
                                            mode='circular')
        # 获取输入x的尺寸：
        batch_size, in_channels, height, width = x.size()
        # 获取权重的尺寸
        out_channels, _, kernel_size, _ = self.weight.size()
        # 计算特征值的高宽
        output_height = (height - kernel_size) // self.stride + 1
        output_width = (width - kernel_size) // self.stride + 1
        # 创建output特征图的空张量
        output = torch.zeros(batch_size, out_channels, output_height, output_width)
        # 卷积操作：遍历输出特征图, 获取每个位置的感受野receptive_field,与权重weight相乘并求和,再加上bias得到输出
        for i in range(output_height):
            for j in range(output_width):
                # 获取每个位置的感受野receptive_field
                receptive_field = x[:, :, i * self.stride:i * self.stride + kernel_size,
                                  j * self.stride:j * self.stride + kernel_size]
                # 感受野receptive_field与权重weight相乘并求和,再加上bias得到输出
                output[:, :, i, j] = torch.sum(receptive_field * self.weight.unsqueeze(0),
                                               dim=(1, 2, 3)) + self.bias.unsqueeze(0)
        return output


# 自定义ReLU激活函数
class ReLU(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input):
        """
        实现ReLU的前向计算过程
        """
        # 将输入中的负值阶段为0, 其余不变
        return input.clamp(min=0)


# 自定义全连接层
class Linear(nn.Module):
    def __init__(self, in_features, out_features):
        # 保证兼容性的继承
        super(Linear, self).__init__()
        self.in_features = in_features
        self.out_features = out_features
        # 创建权重和偏置参数并注册为Parameter
        self.weight = nn.Parameter(torch.Tensor(out_features, in_features))
        self.bias = nn.Parameter(torch.Tensor(out_features))
        # 调用初始化参数的方法
        self.reset_parameters()

    # 初始化权重方法
    def reset_parameters(self):
        # 按K-mean均值方法初始化权重,以a为下限
        nn.init.kaiming_uniform_(self.weight, a=math.sqrt(5))
        # 计算w的fan_in用于初始化偏置bias
        fan_in, _ = nn.init._calculate_fan_in_and_fan_out(self.weight)
        # bound与fan_in的开平方呈反比
        bound = 1 / math.sqrt(fan_in)
        # 从均匀分布[-bound, bound]中抽样bias的值
        nn.init.uniform_(self.bias, -bound, bound)

    # 定义前向传播方法
    def forward(self, input):
        # 实现线性变换,返回输出
        return torch.mm(input, self.weight.t()) + self.bias


# 自定义Adam优化器
class Adam(Optimizer):
    # 初始化方法,设置默认参数值 lr:学习率 betas：控制动量衰减,较大时增加优化器的稳定性,平滑参数的更新 eps:当分母为0时,保证不会爆炸
    # weight_decay：权重衰减系数,主要用于过拟合控制
    def __init__(self, params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=0):
        # params：所有需要优化的参数
        super().__init__(params)
        # 创建一个包含所有参数的字典defaults
        self.defaults = dict(lr=lr, betas=betas, eps=eps, weight_decay=weight_decay)
        # 遍历参数组，param_groups是从父类Optimizer继承来的属性，Adam自动处理为包含了所有参数组的列表
        """
           [{'params': [model.param1, model.param2], 
             'lr': 0.001, 
             'betas': (0.9, 0.999), 
             'eps': 1e-08, 
             'weight_decay': 0},
            {'params': [model.param2], 
             'lr': 0.001, 
             'betas': (0.9, 0.999), 
             'eps': 1e-08, 
             'weight_decay': 0}] 
        """
        for group in self.param_groups:
            # 遍历每个组中的参数p：[model.param1, model.param2]
            for p in group['params']:
                # 获取参数p对应的状态state，是Optimizerz父类中的属性，用于储存每个参数的状态
                state = self.state[p]
                # 初始化步长:会累加，用于衰减β1和β2的值(betas)
                state['step'] = 0
                # 初始化一阶动量估计，值为与p.data大小相同的全0张量:会根据β1进行衰减，并添加新的一阶动量估计
                state['exp_avg'] = torch.zeros_like(p.data)
                # 初始化二阶动量估计，值为与p.data大小相同的全0张量:会根据β2进行衰减，并添加新的二阶动量估计
                state['exp_avg_sq'] = torch.zeros_like(p.data)
                # 根据state['exp_avg'], state['exp_avg_sq']计算出学习率，来更新参数p

    # 定义优化一步的方法step()，用于更新参数
    def step(self, closure=None):
        # 初始化损失值loss为None:有些优化器在更新参数时需要损失值
        loss = None
        # 如果提供了closure函数,则调用它来获得损失值loss并赋值给loss:使优化器能够兼容需要损失值的场景
        if closure is not None:
            loss = closure()
        # 遍历每个参数组group:定义优化器时可能传入多个参数组
        for group in self.param_groups:
            # 遍历每个参数组group中的每个参数p:更新每个参数组中的每个参数
            for p in group['params']:
                # 如果参数p的梯度grad为None,则跳过它:无法更新没有梯度的参数
                if p.grad is None:
                    continue
                # 如果p有梯度,则将grad移动到p所在的设备device上:方便后续的计算
                grad = p.grad.data.to(p.device)
                # 获取参数p对应的状态state
                state = self.state[p]
                # 从状态state中取出一阶动量估计exp_avg,二阶动量估计exp_avg_sq:用于计算参数更新量
                exp_avg, exp_avg_sq = state['exp_avg'], state['exp_avg_sq']
                # 从参数组中取出β1和β2的值:用于计算参数更新量
                beta1, beta2 = group['betas']
                # 参数p的步数state['step']加1，步数用于衰减β1和β2的值
                state['step'] += 1
                # 更新exp_avg:用β1衰减之前的值,再加上当前梯度grad,权重为1-β1
                exp_avg.mul_(beta1).add_(grad, alpha=1 - beta1)  # 计算一阶动量估计
                # 更新exp_avg_sq:用β2衰减之前的值,再加上当前梯度grad的平方,权重为1 - β2
                exp_avg_sq.mul_(beta2).addcmul_(grad, grad, value=1 - beta2)  # 计算二阶动量估计
                # denom是学习率lr的分母,为exp_avg_sq的平方加上'eps':'eps' 用于数值稳定
                denom = exp_avg_sq.sqrt().add_(group['eps'])  # 计算分母
                # 计算修正系数bias_correction1和bias_correction2:Adam算法中的特点，用于修正动量估计的偏差
                bias_correction1 = 1 - beta1 ** state['step']
                bias_correction2 = 1 - beta2 ** state['step']
                # 计算学习率step_size,由学习率lr、修正系数bias_correction1和bias_correction2共同决定。这是Adam独有的学习率计算方式。
                step_size = group['lr'] * math.sqrt(bias_correction2) / bias_correction1
                # 用计算得到的学习率step_size更新参数p,不计算梯度。这是为了避免更新参数时的梯度计算,提高效率
                with torch.no_grad():
                    p.data.addcdiv_(exp_avg, denom, value=-step_size)  # 参数更新
        # 返回损失值:为了兼容需要返回损失值的场景
        return loss

# 自定义交叉熵损失函数
class CrossEntropyLoss(nn.Module):
    def __init__(self):
        super().__init__()

    
    def forward(self, input, target):
        """
        input: 预测概率,形状为(batch_size, num_classes)
        target: 真实标签,形状为(batch_size)
        return: loss
        """
        log_softmax = nn.LogSoftmax(dim=1)
        log_prob = log_softmax(input)
        loss = torch.mean(torch.sum(-target * log_prob, 1))
        return loss

# 神经网络
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        # 卷积层 升通道 丢特征
        self.conv_layer = nn.Sequential(
            Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1), ReLU(),
            Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1), ReLU(),
            Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1), ReLU(),
            Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1), ReLU(),
            Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1), ReLU(),
            Conv2d(in_channels=128, out_channels=256, kernel_size=3, stride=1)
        )
        # 全连接层 输出层
        self.out_layer = nn.Sequential(
            Linear(256 * 26 * 26, 10)
        )
        
    # 前向训练
    def forward(self, x):
        x = self.conv_layer(x)
        # 数据展平
        x = x.reshape(-1, 256 * 26 * 26)
        return self.out_layer(x)


# 训练器
class Trainer:
    def __init__(self):
        # 隐式地继承了_LRScheduler基类
        super().__init__()
        # 初始化tensorboard,用于上传训练结果至可视化平台Tensorboard
        self.summerWriter = SummaryWriter("logs")
        # 读取训练集
        self.train_dataloader = DataLoader(dataset=cifar10_train, batch_size=1024, shuffle=True)
        # 读取测试集
        self.test_dataloader = DataLoader(dataset=cifar10_test, batch_size=1024, shuffle=True)
        # 定义设备
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        # 将网络放入设备
        self.net = Net().to(self.device)
        # 初始化优化器
        self.opt = Adam(self.net.parameters(), lr=0.001)
        # 定义损失函数为交叉熵损失函数
        self.fc_loss =