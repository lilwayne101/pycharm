
import numpy as np
import torch.nn as nn
import torch
from torchvision import datasets, transforms
import torchvision.datasets.mnist as mnist
import os
from skimage import io
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

# 迭代：数据，标签
# for i, (img, label) in enumerate(zip(train_set[0], train_set[1])):
#     # 构建路径
#     # print(f"{train_path}")
#     # exit()
#     path = f"{train_path}//{label}//{i}.jpg"
#     if not os.path.exists(f"{train_path}//{label}"):
#         os.makedirs(f"{train_path}//{label}")
#     # 数据的写操作
#     io.imsave(path, np.array(img))

# 测试集
# for i, (img, label) in enumerate(zip(test_set[0], test_set[1])):
#     # 构建路径
#     path = f"{test_path}//{label}//{i}.jpg"
#     if not os.path.exists(f"{test_path}//{label}"):
#         os.makedirs(f"{test_path}//{label}")
#     # 数据的写操作
#     io.imsave(path, np.array(img))

class MNIST_Net(nn.Module):
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
        self.fc_layer(x)
        39:26
