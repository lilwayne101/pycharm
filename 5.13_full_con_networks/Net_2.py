import os

import numpy as np
from torch import optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import torch.nn as nn
import torch
from torch.utils.tensorboard import SummaryWriter

transform = transforms.Compose(
    # 将数据格式转为Tensor(范围为(0-1))
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
)

root = r"E:\data\Cifar10"
os.makedirs(root, exist_ok=True)
cifar10_train = datasets.CIFAR10(root=root, train=True, transform=transforms.ToTensor(), download=True)
cifar10_test = datasets.CIFAR10(root=root, train=False, transform=transforms.ToTensor(), download=True)



# 神经网络
class NetV1(nn.Module):
    def __init__(self):
        super().__init__()
        # 卷积层 升通道 丢特征
        self.conv_layer = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1, padding_mode="zeros"), nn.ReLU(),
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1), nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1), nn.ReLU(),
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1), nn.ReLU(),
            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, stride=1)
        )
        # 全连接层 输出层
        self.out_layer = nn.Sequential(
            nn.Linear(256 * 26 * 26, 10)
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
        super().__init__()
        # 初始化tensorboard
        self.summerWriter = SummaryWriter("logs")
        # 读取训练集
        self.train_dataloader = DataLoader(dataset=cifar10_train, batch_size=256, shuffle=True)
        # 读取测试集
        self.test_dataloader = DataLoader(dataset=cifar10_test, batch_size=256, shuffle=True)
        # 定义设备
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        # 将网络放入设备
        self.net = NetV1().to(self.device)
        # 初始化优化器
        self.opt = optim.Adam(self.net.parameters(), lr=0.001)
        # 定义损失函数为交叉熵损失函数
        self.fc_loss = nn.CrossEntropyLoss()
        # 定义模型参数保存和加载路径
        self.params_dir = r"./params"
        os.makedirs(self.params_dir, exist_ok=True)

    def train(self):
        for epoch in range(1, 10000):
            # 轮次
            # 总损失
            sum_loss = 0
            # 循环每批次的数据
            for i, (img, target) in enumerate(self.train_dataloader):
                # 操作模式，启动训练模式
                self.net.train()
                # 将数据和标签放入cuda中
                img, target = img.to(self.device), target.to(self.device)
                # 获取神经网络输出结果
                out = self.net(img)
                # 将输出结果和标签用损失函数得出损失
                loss = self.fc_loss(out, target)
                # 清空梯度
                self.opt.zero_grad()
                # 反向更新
                loss.backward()
                # 调用优化器更新参数
                self.opt.step()
                # 计算总损失
                sum_loss += loss.item()
                # 储存一次参数
                if epoch % 100 == 0:
                    torch.save(self.net.state_dict(), f"{self.params_dir}/model_{epoch}.pth")
            # 每轮次的平均损失
            avg_loss = sum_loss / len(self.train_dataloader)
            # 每轮次的平均损失记录到tensorboard
            self.summerWriter.add_scalar("训练损失", avg_loss, epoch)
            print(f"第{epoch}轮次的损失为{avg_loss}")

    def test(self):
        # 读取最新一次的参数
        latest_model_path = os.path.join(self.params_dir, sorted(os.listdir(self.params_dir))[1])
        # print(latest_model_path)
        self.net.load_state_dict(torch.load(latest_model_path))
        # 测试轮次
        for epoch in range(1, 101):
            # 每轮次的总分
            sum_score = 0
            # 按批次循环测试集
            for i, (img, target) in enumerate(self.test_dataloader):
                # 开启测试模式
                self.net.eval()
                # 将测试集和标签放入cuda
                img, target = img.to(self.device), target.to(self.device)
                # 将测试集放入网络
                h = self.net(img)
                # 获取预测值
                a = torch.argmax(h, dim=1)
                score = torch.mean(torch.eq(a, target).float())
                # 每批次的得分和
                sum_score += score.item()
            # 每轮次的平均得分
            avg_score = sum_score / len(self.test_dataloader)
            print(len(self.test_dataloader))
            # 将每轮次的平均分数加进tensorboard
            self.summerWriter.add_scalar(f"第{epoch}轮次测试得分", avg_score, epoch)
            print(f"第{epoch}轮次的得分{avg_score}")


if __name__ == "__main__":
    trainer = Trainer()
    trainer.train()
    # trainer.test()


