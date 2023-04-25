import math

import numpy as np
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
x = np.arange(-10, 10, 0.01)
y = np.tanh(x)
plt.plot(x, y)
plt.show()
plt.close()


# Softmax(归一化指数函数)(输出函数)

