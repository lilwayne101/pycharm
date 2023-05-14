import cv2
import numpy as np
import torch.nn as nn
import torch
import torch.optim
from torch.utils.data import Dataset
from torch.utils.data import _utils
from torchvision import datasets, transforms
import torchvision.datasets.mnist as mnist
import os
from skimage import io
from  torch.utils.tensorboard import SummaryWriter
# NCHW结构
# NV结构 (NCHW结构的数据展平)

# train 训练
# test测试
# transform = transforms.ToTensor(): 转化为张量, 归一化[0, 1], CHW
# train_dataset = datasets.MNIST(root=r"H:\data", train=True, transform=transforms.ToTensor(), download=True)
# test_dataset = datasets.MNIST(root=r"H:\data", train=False, transform=transforms.ToTensor(), download=True)
# print(train_dataset.data.shape)
# print(test_dataset.data.shape)
# print(train_dataset.data[0])
# print(train_dataset.targets[0])
# img1 = train_dataset.data[0]
# img1 = transforms.ToPILImage()(img1)
# img1.show()

root = r"H:\data\MNIST"
train_set = mnist.read_image_file(os.path.join(root, "train-images-idx3-ubyte")),\
    mnist.read_label_file(os.path.join(root, "train-labels-idx1-ubyte"))
test_set = mnist.read_image_file(os.path.join(root, "t10k-images-idx3-ubyte")),\
    mnist.read_label_file(os.path.join(root, "t10k-labels-idx1-ubyte"))

# 训练集
train_path = os.path.join(root, "train")
if not os.path.exists(train_path):
    os.makedirs(train_path)
# 测试集
test_path = os.path.join(root, "test")
if not os.path.exists(test_path):
    os.makedirs(test_path)

# 创建数据集和测试的数据文件
# # 迭代：数据，标签
# for i, (img, label) in enumerate(zip(train_set[0], train_set[1])):
#     # 构建路径
#     # print(f"{train_path}")
#     # exit()
#     path = f"{train_path}//{label}//{i}.jpg"
#     if not os.path.exists(f"{train_path}//{label}"):
#         os.makedirs(f"{train_path}//{label}")
#     # 数据的写操作
#     io.imsave(path, np.array(img))
#
# # 测试集
# for i, (img, label) in enumerate(zip(test_set[0], test_set[1])):
#     # 构建路径
#     path = f"{test_path}//{label}//{i}.jpg"
#     if not os.path.exists(f"{test_path}//{label}"):
#         os.makedirs(f"{test_path}//{label}")
#     # 数据的写操作
#     io.imsave(path, np.array(img))


# 神经网络
class MnistNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc_layer = nn.Sequential(
            nn.Linear(1 * 28 * 28, 512), nn.ReLU(),
            nn.Linear(512, 256), nn.ReLU(),
            nn.Linear(256, 128), nn.ReLU(),
            nn.Linear(128, 64), nn.ReLU(),
            nn.Linear(64, 10),
            nn.Softmax(dim=1),
        )

    def forward(self, x):
        return self.fc_layer(x)



# 数据集
class MnistDataset(Dataset):
    # 初始化数据集
    def __init__(self, root, is_train=True):
        super().__init__()
        self.dataset = []
        train_or_test = "train" if is_train else "test"
        # 路径
        path = f"{root}//{train_or_test}"
        for label in os.listdir(path):
            for img_path in os.listdir(f"{path}//{label}"):
                # H:\data\MNIST//train//0//1.jpg
                self.dataset.append((f"{path}//{label}//{img_path}", label))

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        # enumerate()调用时
        # 把路径读取成图像,归一化
        data = self.dataset[index]
        # opencv 读取
        img = cv2.imread(data[0], 0)
        img = img.reshape(-1)  # [0, 255]
        img = img / 255
        # 标签5 ---> one-hot
        one_hot = np.zeros(10)
        one_hot[int(data[1])] = 1
        return np.float32(img), np.float32(one_hot)
        pass


# 数据训练和测试
class Trainer:
    def __init__(self):
        super().__init__()
        # 判断当前环境是否有cuda
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(self.device)

        # 网络
        self.net = MnistNet()
        # net 放入cuda或cpu
        self.net.to(self.device)
        # 轮次：把数据集全部训练一遍
        # 批次：一次性放入cuda的数据量是多少个？
        # 一轮数据需要多少批次
        self.train_dataset = MnistDataset(root, is_train=True)
        self.train_loader = torch.utils.data.DataLoader(dataset=self.train_dataset, batch_size=30000, shuffle=True)
        self.test_dataset = MnistDataset(root, is_train=False)
        self.test_loader = torch.utils.data.DataLoader(dataset=self.test_dataset, batch_size=30000, shuffle=True)
        # 模型训练完成，得到h，loss，反向更新，优化器去优化模型的权重
        self.opt = torch.optim.Adam(self.net.parameters())
        self.summerWriter = SummaryWriter("logs")

    def train(self):
        for epoch in range(10000):
            sum_loss = 0
            # 60000
            for i, (img, label) in enumerate(self.train_loader):
                # 模式操作，打开训练模式
                self.net.train()
                img, label = img.to(self.device), label.to(self.device)
                # 前向计算
                h = self.net(img)
                # 求损失
                # (均方差)万能损失函数：回归/分类，效率高
                loss = torch.mean((h - label) ** 2)
                # 梯度更新
                # 清空梯度
                self.opt.zero_grad()
                # 反向更新
                loss.backward()
                self.opt.step()
                sum_loss += loss
                if i % 10 == 0:
                    torch.save(self.net.state_dict(), f"params//{i}.pth")
            avg_loss = sum_loss / len(self.train_loader)
            self.summerWriter.add_scalar("训练损失", avg_loss, epoch)
            print(f"第{epoch}轮次的损失{avg_loss}")

    def test(self):
        # 把最优的训练效果进行测试
        self.net.load_state_dict(torch.load(r"params//" + os.listdir(r"params")[-1]))
        for epoch in range(10000):
            sum_score = 0
            for i, (img, label) in enumerate(self.test_loader):
                # 开启测试模式
                self.net.eval()
                img, label = img.to(self.device), label.to(self.device)
                h = self.net(img)
                # h是计算答案(10分类，10个概率值)，label标答(one-hot)
                # NV结构
                # [0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.82]
                a = torch.argmax(h, dim=1)
                # [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
                b = torch.argmax(label, dim=1)
                score = torch.mean(torch.eq(a, b).float())
                sum_score += score
            avg_score = sum_score / len(self.test_loader)
            self.summerWriter.add_scalar("测试得分", avg_score, epoch)
            print(f"第{epoch}轮次的得分{avg_score}")


if __name__ == "__main__":
    trainer = Trainer()
    trainer.train()
