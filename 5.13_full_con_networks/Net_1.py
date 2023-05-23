import numpy as np
import torch
import torch.nn as nn

# 全连接层 (输入数据)
net1 = nn.Linear(3 * 32 * 32, 512)
# 卷积层 (没有输入数据,只有通道)
net2 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1)

# 1572864 512
# [print(p.numel()) for p in net1.parameters()]
# 27 1
# [print(p.numel()) for p in net2.parameters()]

print(net2.bias.numel())
print(net2.weight.numel())