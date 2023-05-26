import cv2
import numpy as np
from PIL import Image

"""
    1 找到被打开的图像位置
    2 读取图像并打开
    3 显示
"""
# img_test = Image.open('OIP-C.jpg')
# WHC
# print(img_test.size)

# 创建一个窗口命名
# cv2.namedWindow('img', cv2.WINDOW_NORMAL)
# 设置窗口（img）的大小
# cv2.resizeWindow('img', 400, 400)
# 找到被打开图像位置
img = cv2.imread('OIP-C.jpg')
# 通道分离
b, g, r = cv2.split(img)
# (217, 204, 3)
# HWC
# print(img.shape)
# 参数1：图像显示的窗口名
# 参数2：显示的具体图像
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
cv2.imshow('img', img)

# 通道的合并
imgC = cv2.merge((b, g, r))
# 当要显示图片的时候，会默认的创建一个窗口
cv2.imshow('imgC', imgC)

# 等待按键按下 大于0 表示演示ms
# 如果是0 表示一直等待按键按下
key = cv2.waitKey(0)
if key == ord('q'):
    print(key)
    # 窗口释放
    cv2.destroyAllWindows()
    pass
# 窗口释放

