import math

import cv2
import numpy as np
import torch
from matplotlib import pyplot as plt

# 幂函数
# x = np.arange(-10, 10, 0.01)
# # y1 = x ** 2
# y2 = np.power(x, 3)
# # y3 = pow(x, 4)
# # y4 = math.pow(2, 3)
# # plt.plot(x, y1)
# plt.plot(x, y2)
# # plt.title("x ** 3")
# # plt.plot(x, y3)
# # print(f"{y4}")
# plt.show()
# plt.close()

# <class 'complex'>
# j = 10 - 8j

# 指数函数
# x = np.linspace(-10, 10, 1000)
# y1 = 2 ** x
# y2 = np.exp(x)
# y3 = np.exp2(x)   # 2 ** x
# y4 = np.expm1(x)  # np.exp(x) -1
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)
# plt.plot(x, y4)
# plt.show()
# plt.close()

# 激活函数
# sigmoid 函数
# x = np.arange(-10, 10, 0.01)
# sigmoid = 1 / (1 + np.exp(-x))
# dsigmoid = sigmoid * (1 - sigmoid)  # 求sigmoid的导函数
# plt.plot(x, sigmoid)
# plt.plot(x, dsigmoid)
# plt.show()

# Relu 函数
# x = np.arange(-10, 10, 0.1)
# y = np.maximum(0, x)
# plt.plot(x, y)
# plt.show()

# tanh(双曲正切)
# x = np.arange(-10, 10, 0.01)
# y = np.tanh(x)
# plt.plot(x, y)
# plt.show()
# plt.close()


# Softmax(归一化指数函数)(输出函数)

# import torch
#
# t1 = torch.


# t1 = torch.Tensor([1, 2, 3])
# t2 = torch.FloatTensor([1, 2, 3])
# t3 = torch.tensor([1, 2, 3], dtype=torch.long)
# t4 = torch.tensor([1, 2, 3])
# # torch.float32
# print(t1.dtype)
# # torch.float32
# print(t2.dtype)
# # torch.int64
# print(t3.dtype)
# # torch.int64
# print(t4.dtype)
# # torch.int32
# print(t1.int().dtype)
# # torch.float64
# print(t1.type(torch.float64).dtype)

# a = torch.Tensor([[[1, 2, 3], [7, 8, 9]], [[4, 5, 6], [1, 1, 1]]])  # 2 * 2 * 3
# a = a.reshape(2, 6)
# a = a.view(2, 6)
# a = a.reshape(-1)
# print(a)
# a = a.reshape(-1, 3)
# print(a)
# a = a.reshape(-1, 3, 2)
# print(a)

# tensor 和 numpy的类型转换
# data = [[1, 2], [3, 4]]
# t = torch.tensor(data)
# print(t)
# n = np.array(data)
# print(n)
# t = torch.tensor(n)
# print(t)
# n1 = t.numpy()
# print(n1)
# n2 = torch.from_numpy(n1)
# print(type(n))
# print(type(t))
# print(type(n1))
# print(type(n2))

# 张量的声明
# a = torch.empty(5, 3)
# b = torch.rand(5, 3)
# c = torch.zeros(5, 3, dtype=torch.long)
# d = torch.ones(5, 3, dtype=torch.long)
# print(a)
# print(b)
# print(c)
# print(d)
# print(a.size())
# print(b.size())
# print(c.size())
# print(d.size())

# CPU张量和GPU张量之间的转换
# tensor = torch.rand(3, 4)
# print(f"1tensor的形状：{tensor.shape}")
# print(f"2tensor的数据类型：{tensor.dtype}")
# print(f"3tensor的运算形式：{tensor.device}")
# tensor = tensor.cuda()
# print(f"4tensor的运算形式：{tensor.device}")
# tensor = tensor.cpu()
# print(f"5tensor的运算形式：{tensor.device}")

# a = torch.Tensor([[[1, 2, 3], [7, 8, 9]], [[4, 5, 6], [1, 1, 1]]])
# print(a.sum(dim=0))
# print(a.sum(dim=1))
# print(a.sum(dim=2))

# multiply() mul() (多维)
# t1 = torch.arange(8).reshape(2, 4)
# t2 = torch.arange(9, 17).reshape(2, 4)
# print(t1)
# print(t2)
# print(torch.multiply(t1, t2))   # mul()平替

# torch.mm()二维 matmul()高维 矩阵相乘
# a = torch.arange(1, 7).reshape(2, 3)
# b = torch.arange(7, 13).reshape(3, 2)
# c = torch.mm(a, b)
# print(a)
# print(b)
# print(c)

# dot
# t1 = torch.tensor([1, 2, 3])
# t2 = torch.tensor([4, 5, 6])
# print(torch.dot(t1, t2))

# 转置
# a = torch.arange(1, 5).reshape(2, 2)
# print(a)
# print(a.T)

# 连接
# a = torch.tensor([[1], [2]])
# b = torch.tensor([[3], [4]])
# c = torch.cat([a, b], 0) # 按行连接,谁上谁下
# d = torch.cat([a, b], 1)  # 按列连接,谁左谁右
# print(c)
# print(d)

# 压缩
# x = torch.zeros(2, 1, 2, 1, 2)
# print(x)
# print(x.size())
# print(torch.squeeze(x))
# print(torch.squeeze(x).size())

# 拆分
# x = torch.arange(1, 10).reshape(3, 3)
# print(x)
# a, b, c = x.split(1, 0)    # 在零维进行间隔为1的拆分
# print(a)
# print(b)
# print(c)
# a, b, c = x.split(1, 1)    # 在一维进行间隔为1的拆分
# print(a)
# print(b)
# print(c)

# softmax归一化指数：概率
# index = torch.argmax(torch.tensor([0.1, 0.05, 0.15, 0, 0, 0, 0, 0, 0, 0.7]))
# print(index)
# one_hot = torch.zeros(10)
# one_hot[index] = 1
# print(one_hot)
# y = torch.tensor([0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
# b = torch.eq(one_hot, y)
# print(b)

# 伯努利分布
import random
# print(random.random() > 0.5)


# 大数定律
# def sumT(count):
#     k = 0
#     for i in range(count):
#         if random.random() > 0.5:
#             k += 1
#     print(k / count)
#
# sumT(10000)

# 正态分布
# from scipy import stats
# mean = 0
# sd = 1
# x = np.arange(-10, 10, 0.1)
# y = stats.norm.pdf(x, mean, sd)
# plt.plot(x, y)
# plt.title(f"mu:{mean} -- sd:{sd}")
# plt.grid()
# plt.show()


import torch.nn as nn
from torch import optim

#
# # 交叉熵损失函数(多分类)
# nn.CrossEntropyLoss()
# # 二分类交叉熵损失函数
# nn.BCELoss()

# 信息熵
# data1 = [0.5, 0.6, 0.7, 1, 0.5]
# data2 = [0.1, 0.2, 0.3, 0.4, 0.5]
#
# def get_cent(data):
#     sum = 0.
#     for d in data:
#         sum -= d * np.log(d)
#     return sum
# print(get_cent(data1))
# print(get_cent(data2))

# p = [(0.1, 0.2, 0.3, 0.4), (0.1, 0.6, 0.7, 0.8)]
# ce = np.sum(np.float())


# def per(w, x, b):
#     w = np.array(w)
#     x = np.array(x)
#     return np.sum(w * x) + b


# 感知机
# x = [120, 130, 150, 180, 200]
# x1 = np.array([120, 130, 150, 180, 200])
# x1 = (x1 / 255) - 0.5
# w = [0.1, 0.15, 0.12, 0.05, 0.08]
# b = 0.05
# h1 = per(w, x, b)
# h = per(w, x1, b)
# # print(h1)
# # print(h)
# print((h + 0.5) * 255)
# h = nn.Softmax(dim =0)(torch.tensor(h))
# print(h)

# print(np.hstack(([1, 2, 3], [4, 5, 6])))
# print(np.hstack((1, 4)))
# print(np.hsplit(np.array([1, 2, 3, 4]), 2))

# one-hot编码
# index = [1, 2, 3, 4, 5, 7, 7, 5, 3]
# one_hots = np.eye(10)[index]
# print(one_hots)

# a = torch.randn(3, 5)
# b = torch.randn(3, 5)
# print(torch.nn.MSELoss()(a, b))
# print(torch.nn.functional.mse_loss(a, b))
# # print(torch.mean((a - b) ** 2))

# # 多分类交叉熵，自带Softmax输出函数
# torch.nn.CrossEntropyLoss()
# # 多分类交叉熵，不带输出函数，需要用Softmax()激活
# torch.nn.NLLLoss()
#
# # 二分类交叉熵，自带Sigmoid输出函数
# torch.nn.BCEWithLogitsLoss()
# # 不带激活函数
# torch.nn.BCELoss()

# 继承神经网络基类
# class Net(nn.Module):
#     def __init__(self):
#         super().__init__()
#         # 神经网络序列构造器
#         self.layer = nn.Sequential(
#             # 构造神经网络的每一层
#             # (128, 3 * 274 * 360) -->(128, 1024)
#             nn.Linear(in_features=3 * 274 * 360, out_features=1024, bias=False),
#             # (128, 1024) -->(128, 512)
#             nn.Linear(1024, 512),  # 特征压缩()
#             nn.Linear(512, 256),
#             nn.Linear(256, 128),
#             nn.Linear(128, 64),
#             # (128, 64)-->(128, 2)
#             nn.Linear(64, 2),
#             # 2 分类，输出函数，NV结构
#             # (128, 2)-->(128, 2)
#             # nn.Softmax(dim=1)
#             nn.Sigmoid()
# )
#     # 前向计算(FP)
#     # x：输入网络的数据
#     def forward(self,x):
#         return self.layer(x)
#
#
# if __name__ == "__main__":
#     net = Net()
#     print(net)
#     # NV结构
#     data = torch.randn(10, 3 * 274 * 360)
#     h = net.forward(data)
#     # torch.Size([10, 2])
#     print(h.shape)
#     print(h)


# class Mynet(nn.Module):
#
#     def __init__(self):
#         super().__init__()
#         # mnist数据集(1*28*28)
#         self.fc_layer1 = nn.Linear(784, 128)
#         self.relu1 = nn.ReLU()
#         self.fc_layer2 = nn.Linear(128, 64)
#         self.relu2 = nn.ReLU()
#         self.fc_layer3 = nn.Linear(64, 2)
#         self.softmax = nn.Softmax(dim=1)
#
#     def forward(self, x):
#         x = self.fc_layer1(x)
#         x = self.relu1(x)
#         x = self.fc_layer2(x)
#         x = self.relu2(x)
#         x = self.fc_layer3(x)
#         return self.softmax(x)
#
#
# if __name__ == "__main__":
#     net = Mynet()
#     data = torch.randn(10, 784)
#     h = net.forward(data)
#     print(h.shape)
#     # print(net)
#     print(h)


# import torch
# import torch.nn as nn
# import torch.nn.functional as F
#
# # 构建分类模型
# model = nn.Sequential(
#     nn.Linear(3, 3),
#     nn.Softmax()
# )
#
# # 定义交叉熵损失函数
# criterion = nn.CrossEntropyLoss()
#
# # 生成模拟数据
# inputs = torch.tensor([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
# labels = torch.tensor([2, 0, 1])
#
# # 定义优化器,这里使用SGD
# optimizer = optim.SGD(model.parameters(), lr=0.01)
#
# # 梯度下降步骤中清零参数的梯度
# optimizer.zero_grad()
#
# # 根据模型输出和 ground truth 计算Loss
# outputs = model(inputs)
# loss = criterion(outputs, labels)
#
# # 反向传播计算梯度
# loss.backward()
#
# # 使用优化器更新参数
# optimizer.step()
#
# # 输出Loss
# print(loss)
# # tensor(1.1772, grad_fn=<NllLossBackward>)

# # XOR前馈网络
# # 创建训练数据
# # 输入有两个特征值
# D = 2
# # 定义输入X
# # (4, 2)
# X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# # 定义目标T
# # (4, 1)
# T = np.array([[0], [1], [1], [0]])
#
#
# # 定义激活函数Sigmoid()函数 用于输出层， 将值压缩到0-1区间，适合未分类问题
# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))
#
#
# # 定义激活函数Relu
# def relu(x):
#     return np.maximum(0, x)
#
#
# # 初始化权重
# # np.random.randn()：产生随机正态分布数，用来初始化w1和w2
# # np.sqrt()计算平方根, 这是Xavier初始化方法，可以避免梯度爆炸(梯度过大)或梯度消失(梯度为0)
# w1 = np.random.randn(D, 3) / np.sqrt(D)     # (2, 3)
# # np.zeros()创建全0数组,这里用于偏执b1的初始化
# b1 = np.zeros((1, 3))   # (1, 3)
# w2 = np.random.randn(3, 1) / np.sqrt(3)     # (3, 1)
# b2 = 0
#
# # 前向传播
# a1 = X.dot(w1) + b1    # (4, 2) * (2, 3) + (1, 3) ---> (4, 3)
#
# """
# [[0.5        0.5        0.5       ]
#  [0.6353178  0.67516274 0.82683442]
#  [0.54106523 0.27767439 0.3008182 ]
#  [0.67254773 0.44413487 0.67259634]]
# """
# # z1 = sigmoid(a1)    # (4, 3) ---> (4, 3)
# z1 = relu(a1)
# print(z1)
# """
# [[-0.00607235]
#  [ 0.06135837]
#  [ 0.12685384]
#  [ 0.17380995]]
# """
# a2 = z1.dot(w2) + b2    # (4, 3) * (3, 1) + 0---> (4, 1)
#
# """
# [[0.66432295]
#  [0.65725995]
#  [0.67109316]
#  [0.66503364]]
# """
# # y = sigmoid(a2)     # (4, 1) ---> (4, 1)
# y = sigmoid(a2)
#
# # 计算损失和梯度
# t = T       # (4, 1)
# # sigmoid()结果 0.6949073561104447
# # relu()结果  0.6906923663845261
# loss = -(t * np.log(y) + (1 - t) * np.log(1 - y)).mean()    # loss = [(1-t)log(1-y) -(tlogy)].mean()

# # 矩阵相乘
# m = np.array([1, 2, 3, 4])
# m1 = m.T
# n = np.array([1, 2, 3, 4])
# r = m * n   # [ 1  4  9 16]
# r1 = m1 * n     # [ 1  4  9 16]
# m2 = np.array([[1, 2, 3], [1, 2, 5]])   # (2, 3)
# m3 = m2.T
# n1 = np.array([[1, 2, 3], [1, 2, 5]])   # (2, 3)
# r2 = m2 * n1    # (2, 3) * (2, 3) --->(2, 3) np的广播机制
# # r3 = m3 * n1    # operands could not be broadcast together with shapes (3,2) (2,3)
# # r4 = np.dot(m2, n1)     # ValueError: shapes (2,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)
# """
# [[ 2  4  8]
#  [ 4  8 16]
#  [ 8 16 34]]
# """
# r3 = np.dot(m3, n1)  # (3, 2) * (2, 3) --->(3, 3)

# img = cv2.imread("H:\data\MNIST//train//8//25445.jpg")
# # data = img.reshape(-1)
# print(img)
# # print(data)
# print(torch.cuda.is_available())

# x = np.arange(-10, 10, 0.01)
# y1 = x ** 2
# y2 = np.power(x, 2)
# y3 = pow(x, 3)
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)
# plt.show()

# x = np.linspace(-10, 10, 2000)
# y1 = np.exp(x)
# y2 = np.exp2(x)
# y3 = np.expm1(x)
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)
# plt.show()

# 对数函数
# x = np.linspace(0.00001, 10, 1000)
# y1 = np.log(x)
# y2 = np.log2(x)
# y3 = np.log10(x)
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)
# plt.show()

# sigmoid
# x = np.arange(-10, 10, 0.001)
# sigmoid = 1 / (1 + np.exp(-x))
# d_sigmoid = sigmoid * (1 - sigmoid)
# plt.plot(x, sigmoid)
# plt.plot(x, d_sigmoid)
# plt.show()

# softmax
# x = np.linspace(-10, 10, 10000)
# softmax = np.exp(x) / np.sum(np.exp(x))
# plt.plot(x, softmax)
# plt.show()

# 数据集
_x = [i * 0.01 for i in range(100)]
# 回归权重w=5, b=5
_y = [x * 5 + 5 + random.random() for x in _x]
# 初始化权重
w = random.random()
b = random.random()
while True:
    for x, y in zip(_x, _y):
        # 预测值
        h = w * x + b
        # loss
        loss = (h - y) ** 2
        # dw, db
        dw = 2 * x * (h - y)
        db = 2 * (h - y)
        # 反向传播,权重更新
        r = 0.001
        w -= dw * r
        b -= db * r
        plt.pause(0.1)
        plt.plot(_x, _y, ".")
        plt.ion()
        plt.plot(x, w * x + b)

    plt.show()


