import numpy as np
from PIL import Image


def mask_make(image, threshold=150):
    # 将图像转为灰度图
    grayscale_image = image.convert("L")
    # grayscale_image.show()

    # 定义二值化转换函数
    def binarize(pixel):
        if pixel > threshold:
            return 0
        else:
            return 255
    binary_image = grayscale_image.point(binarize, mode="1")
    return binary_image


img = Image.open(r"G:\pycharm_not_gitcode\pycharm\pic\3.jpg")
new_img = Image.new("RGB", (400, 400), (100, 100, 100))
# mask_make(img).show()
new_img.paste(img, (0, 0), mask=mask_make(img))
new_img.show()
# new_img = Image.new("RGB", (400, 400), (100, 100, 100))
# new_img.paste(img_t, (0, 0), mask=img)
# new_img.show()

