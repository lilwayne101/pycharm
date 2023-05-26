import cv2
import numpy as np

# 直接创建图像
data = np.full((700, 500, 3), fill_value=(25, 233, 0), dtype=np.uint8)
print(data.shape)
cv2.imshow('img', data)
key = cv2.waitKey(0)
cv2.destroyAllWindows()

