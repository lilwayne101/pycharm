import cv2
import numpy as np


class Cutout:
    def __init__(self):
        self.image = cv2.imread("./image/020.jpg")
        self.window_name = "img"
        cv2.namedWindow(self.window_name, cv2.WINDOW_FREERATIO)

    def color_fill(self):
        # 设置蓝色阈值
        lower_blue = np.array([100, 60, 60])
        upper_blue = np.array([130, 255, 255])
        # 根据阈值构建遮罩
        mask = cv2.inRange(self.image, lower_blue, upper_blue)
        # 形态学操作填充空洞
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        result = cv2.bitwise_and(self.image, self.image, mask=mask)
        return result

    def inter_cutouts(self):
        # 初始化mask
        mask = np.zeros(self.image.shape[:2], np.uint8)
        # 设置ROI
        rect = (0, 0, self.image.shape[0], self.image.shape[1])
        bgd_model = np.zeros((1, 65), np.float64)
        fgd_model = np.zeros((1, 65), np.float64)
        # GrabCut算法
        cv2.grabCut(self.image, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)
        # 根据mask生成抠图结果
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
        result = self.image * mask2[:, :, np.newaxis]
        return result

    def show(self):
        # img = self.color_fill()
        img = self.inter_cutouts()
        # cv2.imshow(self.window_name, self.image)
        cv2.imshow(self.window_name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


cutout = Cutout()
cutout.show()
