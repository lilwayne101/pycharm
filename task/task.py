# import random
# from matplotlib import pyplot as plt
#
# # 数据集
# _x = [i * 0.01 for i in range(100)]
# # 回归权重w=5, b=5
# _y = [x * 5 + 5 + random.random() for x in _x]
# # 初始化权重
# w = random.random()
# b = random.random()
# while True:
#     for x, y in zip(_x, _y):
#         # 预测值
#         h = w * x + b
#         # loss
#         loss = (h - y) ** 2
#         # dw, db
#         dw = 2 * x * (h - y)
#         db = 2 * (h - y)
#         # 反向传播,权重更新
#         r = 0.001
#         w -= dw * r
#         b -= db * r
#         print(f"loss:{loss}\tw:{w},b:{b}")
#         plt.pause(0.1)
#         plt.ion()
#         plt.cla()
#         plt.plot(_x, _y, ".")
#         y = [w * x + b for x in _x]
#         plt.plot(_x, y)
#         plt.show()