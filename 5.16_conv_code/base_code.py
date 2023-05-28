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
from tqdm import tqdm

# 定义 transforms
# 需要注意控制组合转换产生的变化幅度,避免过度扭曲训练输入导致模型学习到不真实的数据分布。这需要根据验证集上的效果进行判断与调整。
transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),  # 以0.5的默认概率执行水平翻转，通过数据增强来缓解过拟合问题并提高模型的泛化能力。
    transforms.RandomVerticalFlip(),    # 以0.5的概率执行垂直翻转
    # 随机旋转图像,参数degrees控制旋转角度的范围。这可以产生更丰富的translations 并增加模型的泛化能力。
    transforms.RandomRotation(degrees=(-45, 45)),
    # 随机裁剪并重新调整图像大小。先随机裁剪出一个区域,然后再调整到指定大小。这可以产生更多变化的图像来训练模型。
    transforms.RandomResizedCrop(size=(32, 32), scale=(0.8, 1)),
    # 随机更改图像的亮度,对比度,饱和度和色调。这可以产生更加丰富的颜色变化来训练模型。
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2),
    # 随机将RGB图像转换为灰度图像。这可以产生更加丰富的输入来训练模型。
    transforms.RandomGrayscale(p=0.2),
    # 将数据格式转为Tensor(范围为(0-1))
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
)


root = r"E:\data\Cifar10"
os.makedirs(root, exist_ok=True)
cifar10_train = datasets.CIFAR10(root=root, train=True, transform=transforms.ToTensor(), download=True)
cifar10_test = datasets.CIFAR10(root=root, train=False, transform=transforms.ToTensor(), download=True)


# 神经网络
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        # 卷积层 升通道
        self.conv_layer = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1),
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1), nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1), nn.ReLU(),
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1), nn.ReLU(),
            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, padding=1)
        )
        # 全连接层 输出层
        self.out_layer = nn.Sequential(
            nn.Linear(256 * 32 * 32, 10)
        )
        
    # 前向训练
    def forward(self, x):
        x = self.conv_layer(x)
        # 数据展平
        x = x.reshape(-1, 256 * 32 * 32)
        return self.out_layer(x)


# 训练器
class Trainer:
    def __init__(self):
        # 隐式地继承了_LRScheduler基类
        super().__init__()
        # 初始化tensorboard,用于上传训练结果至可视化平台Tensorboard
        self.summerWriter = SummaryWriter("logs")
        # 读取训练集
        self.train_dataloader = DataLoader(dataset=cifar10_train, batch_size=128, shuffle=True)
        # 读取测试集
        self.test_dataloader = DataLoader(dataset=cifar10_test, batch_size=128, shuffle=True)
        # 定义设备
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        # 将网络放入设备
        self.net = Net().to(self.device)
        # 初始化优化器
        self.opt = optim.Adam(self.net.parameters(), lr=0.001)
        # 定义损失函数为交叉熵损失函数
        self.fc_loss = nn.CrossEntropyLoss()
        # 定义模型参数保存和加载路径
        self.params_dir = r"./params"
        os.makedirs(self.params_dir, exist_ok=True)

    def train(self):
        score_best = 0
        for epoch in range(1, 1000):
            # 轮次
            # 总损失
            sum_loss = 0
            # 总得分
            sum_score = 0
            # 循环每批次的数据
            ILYSM = tqdm(enumerate(self.train_dataloader), total=len(self.train_dataloader))
            for i, (img, label) in ILYSM:
                # 操作模式,启动训练模式
                self.net.train()
                # 将数据和标签放入cuda中
                img, label = img.to(self.device), label.to(self.device)
                # 获取神经网络输出结果
                out = self.net(img)
                # 将输出结果和标签用损失函数得出损失
                loss = self.fc_loss(out, label)
                # 清空梯度
                self.opt.zero_grad()
                # 反向更新
                loss.backward()
                # 调用优化器更新参数
                self.opt.step()
                # 计算总损失
                sum_loss += loss.item()
                # 获取预测值
                a = torch.argmax(out, dim=1)
                score = torch.mean(torch.eq(a, label).float())
                # 计算总分
                sum_score += score.item()
                ILYSM.set_description(f"{epoch}/{1000}")
            # 存储一次参数
            torch.save(self.net.state_dict(), f"{self.params_dir}/model.pth")
            # 每轮次的平均损失记录到tensorboard
            self.summerWriter.add_scalar("损失", sum_loss / len(self.train_dataloader), epoch)
            self.summerWriter.add_scalar("得分", sum_score / len(self.train_dataloader), epoch)
            sum_score = self.test(epoch, is_test=False)
            if sum_score > score_best:
                torch.save(self.net.state_dict(), f"{self.params_dir}/model_best.pth")
                score_best = sum_score

    def test(self, epoch, is_test):
        sum_score = 0
        sum_loss = 0
        if is_test:
            best_model_path = os.path.join(self.params_dir, "model_best.pth")
            self.net.load_state_dict(torch.load(best_model_path))
        else:
            model_path = f"{self.params_dir}/model.pth"
            self.net.load_state_dict(torch.load(model_path))
        ILYSM = tqdm(enumerate(self.test_dataloader), total=len(self.test_dataloader))
        for i, (img, label) in ILYSM:
            self.net.eval()
            img, label = img.to(self.device), label.to(self.device)
            out = self.net(img)
            loss = self.fc_loss(out, label)
            sum_loss += loss.item()
            a = torch.argmax(out, dim=1)
            b = torch.argmax(label, dim=1)
            score = torch.mean(torch.eq(a, b.float()))
            sum_score += score.item()
        if not is_test:
            self.summerWriter.add_scalar("平均损失", sum_loss / len(self.test_dataloader), epoch)
            self.summerWriter.add_scalar("平均得分", sum_score / len(self.test_dataloader), epoch)
        print(f"第{epoch}轮次的损失:{sum_score / len(self.test_dataloader)}")
        print(f"第{epoch}轮次的得分:{sum_loss / len(self.test_dataloader)}")
        return sum_score


if __name__ == "__main__":
    trainer = Trainer()
    trainer.train()


