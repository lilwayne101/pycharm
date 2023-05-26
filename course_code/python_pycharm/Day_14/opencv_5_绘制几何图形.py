"""
    绘制几何图形
    1 线
    2 矩形
    3 园
"""


import cv2
import numpy as np

# 创建一个图像img
img = cv2.imread("./back.jpg")
# cv2.line(img, (100, 100), (200, 200), color=(255, 0, 0), thickness=1)
# cv2.rectangle(img, (100, 100), (200, 200), color=(0, 255, 255), thickness=-1)
# cv2.circle(img, (150, 150), 50, color=(0, 255, 255), thickness=-1)
# 绘制多边形
# pts = np.array([(100, 100), (200, 200), (100, 200), (200, 100)])
# cv2.polylines(img, [pts], isClosed=True, color=(255, 255, 0), thickness=2)
# cv2.fillPoly(img, [pts], color=(225, 255, 2))

# 绘制文字
# org 绘制文字的坐标必须是整型的
cv2.putText(img, text='卧室', org=(0, 200), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1, color=(255, 0, 0), thickness=2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
