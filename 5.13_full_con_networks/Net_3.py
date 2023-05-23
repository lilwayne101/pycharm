import torch
import torch.nn as nn

conv = torch.nn.Conv2d(in_channels=3, out_channels=6, kernel_size=32,stride=1)
data = torch.randn(128, 3, 32, 32)
data = conv(data)
# print(data.shape)

layer = nn.Conv2d(3, 10, 3, 1)
# (1, 10, 4, 4)
print(layer(torch.randn(1, 3, 6, 6)).shape)
# (3, 10, 10, 10)
print(layer(torch.randn(3, 3, 12, 12)).shape)
# (6, 10, 6, 6)
print(layer(torch.randn(6, 6, 8, 8)).shape)