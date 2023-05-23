import torch.nn as nn
import torch


class Mynet(nn.Module):

    def __init__(self):
        super().__init__()
        # mnist数据集(1*28*28)
        self.fc_layer1 = nn.Linear(784, 128)
        self.relu1 = nn.ReLU()
        self.fc_layer2 = nn.Linear(128, 64)
        self.relu2 = nn.ReLU()
        self.fc_layer3 = nn.Linear(64, 2)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.fc_layer1(x)
        x = self.relu1(x)
        x = self.fc_layer2(x)
        x = self.relu2(x)
        x = self.fc_layer3(x)
        return self.softmax(x)


if __name__ == "__main__":
    net = Mynet()
    data = torch.randn(10, 784)
    h = net.forward(data)
    print(h.shape)
    # print(net)
    print(h)
