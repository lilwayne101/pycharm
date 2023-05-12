import torch.nn as nn
import torch
# 继承神经网络基类


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        # 神经网络序列构造器
        self.layer = nn.Sequential(
            # 构造神经网络的每一层
            # (128, 3 * 274 * 360) -->(128, 1024)
            nn.Linear(in_features=3 * 274 * 360, out_features=1024, bias=False),
            # (128, 1024) -->(128, 512)
            nn.Linear(1024, 512), nn.ReLU(),  # 特征压缩()
            nn.Linear(512, 256),nn.ReLU(),
            nn.Linear(256, 128),nn.ReLU(),
            nn.Linear(128, 64),nn.ReLU(),
            # (128, 64)-->(128, 2)
            nn.Linear(64, 2),
            # 2 分类，输出函数，NV结构
            # (128, 2)-->(128, 2)
            # nn.Softmax(dim=1)
            nn.Sigmoid()
)
    # 前向计算(FP)
    # x：输入网络的数据
    def forward(self,x):
        return self.layer(x)


if __name__ == "__main__":
    net = Net()
    print(net)
    # NV结构
    data = torch.randn(10, 3 * 274 * 360)
    h = net.forward(data)
    # torch.Size([10, 2])
    print(h.shape)
    print(h)

