"""
    人脸识别

    眼睛， 眉毛， 鼻子 嘴巴
    级联分类器

"""
import copy
import cv2
import numpy as np


# 定义一个人脸操作的类
class FaceDetect:
    def __init__(self):
        # 创建一个级联分类器,用来识别人脸使用
        self.faceRects = None
        # self.faceImg = cv2.imread(r".\Image\LENIN3.jpg")
        self.faceImg = None
        self.classifier = cv2.CascadeClassifier()
        # 加载特征文件
        self.classifier.load(r"F:\anaconda3\envs\py37\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml")

    # 人脸矩形区域绘制
    def face_detect(self, img):
        self.faceImg = img
        face_img = self.faceImg
        classifier = self.classifier
        # 识别图像中的人脸  返回矩形区域  使用列表进行存储
        self.faceRects = classifier.detectMultiScale(face_img)
        # print(faceImg)
        # [[76 31 51 51]]   x y w h
        # print(faceRects)
        for x, y, w, h in self.faceRects:
            cv2.rectangle(face_img, (x, y), (x + w, y + h), color=(255, 255, 0), thickness=1)
        # cv2.imshow('img', face_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    # 绘制logo
    def draw_logo(self, logo):
        face_rects = self.faceRects
        # print(face_rects)
        face_img = self.faceImg
        # cv2.imshow("img", face_img)
        # 计算图像的缩放比例
        ratio = logo.shape[0] / logo.shape[1]
        small_logo = None
        for face_rect in face_rects:
            face_x = face_rect[0]
            face_y = face_rect[1]
            face_w = face_rect[2]
            face_h = int(face_rect[3] * ratio)
            # 因为图像比较大,需要缩放
            small_logo = cv2.resize(logo, dsize=(face_w, face_h))
            small_logo_w, small_logo_h = small_logo.shape[:2]
            # print(face_img.shape)
            # print(small_logo.shape)
            # cv2.imshow("logo", small_logo)
            for row in range(small_logo_w):
                for col in range(small_logo_h):
                    if face_y - small_logo_w + row < 0:
                        continue
                    face_img[face_y - small_logo_w + row, face_x + col] = small_logo[row, col]  # 注意：图像和数组维度位置的区别
        return face_img
        # cv2.imshow('smallLogo', smallLogo)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # cv2.imshow('img', face_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    def drawLogoMethod02(self, logo):
        logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
        retval, logo_binary = cv2.threshold(logo_gray, 200, 255, cv2.THRESH_BINARY)
        # retval, logo_binary = cv2.threshold(logo_gray, 200, 255, cv2.THRESH_OTSU)
        # print(retval)
        # 找轮廓
        # 参数2：轮廓的存放层级关系
        # 参数3：存储轮廓的拐角点
        contours, hierarchy = cv2.findContours(logo_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # 绘制轮廓
        # 创建一个黑色背景图
        mask = np.zeros(logo_binary.shape, dtype=np.uint8)
        cv2.drawContours(mask, contours, 0, color=(255, 255, 255), thickness=5)
        # cv2.imshow('logo', logo)
        # cv2.imshow('logo_gray', logo_gray)
        # cv2.imshow('logo_binary', logo_binary)
        # cv2.imshow('mask', mask)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # pass



faceDetect = FaceDetect()
# faceDetect.face_detect()
logo = cv2.imread("./Image/logo.png")
# faceDetect.draw_logo(logo)
faceDetect.drawLogoMethod02(logo)