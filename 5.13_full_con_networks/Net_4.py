from PIL import Image, ImageFilter
import cv2
import torch.nn as nn
from torchvision.transforms import transforms

img = cv2.imread("038.jpg")
conv1 = nn.Conv2d(in_channels=3, out_channels=3, kernel_size=1, stride=1)
img = transforms.ToTensor()(img)
img = conv1(img)
img = transforms.ToPILImage()(img)
img.show(img)