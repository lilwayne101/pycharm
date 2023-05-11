import math

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
# # torch.float32
# print(t1.dtype)
# # torch.float32
# print(t2.dtype)
# # torch.int64
# print(t3.dtype)
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
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        # 神经网络序列构造器
        nn.Sequential(
            # 构造神经网络的第一层
            nn.Linear(3 * 274 * 360, 1024),
            nn.Linear(1024, 512),
            nn.Linear(512, 256),
            nn.Linear(1024, 512),
            nn.Linear(1024, 512),
            nn.Linear(1024, 512),
            nn.Linear(1024, 512),
            nn.Linear(1024, 512),
            nn.Linear(1024, 512),


        )


