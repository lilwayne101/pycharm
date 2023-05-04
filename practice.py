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
t1 = torch.tensor([1, 2, 3])
t2 = torch.tensor([4, 5, 6])
print(torch.dot(t1, t2))


