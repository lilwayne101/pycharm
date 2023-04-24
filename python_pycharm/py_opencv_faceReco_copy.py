"""
    人脸识别

    眼睛， 眉毛， 鼻子 嘴巴
    级联分类器

"""
import copy
import cv2


class FaceDetect:
    def __init__(self):
        # 创建一个级联分类器,用来识别人脸使用
        self.faceRects = None
        self.faceImg = cv2.imread(r".\Image\LENIN3.jpg")
        self.classifier = cv2.CascadeClassifier()
        # 加载特征文件
        self.classifier.load(r"F:\anaconda3\envs\py37\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml")

    # 人脸矩形区域绘制
    def face_detect(self):
        face_img = self.faceImg
        classifier = self.classifier
        # 识别图像中的人脸  返回矩形区域  使用列表进行存储
        self.faceRects = classifier.detectMultiScale(face_img)
        # print(faceImg)
        # [[76 31 51 51]]   x y w h
        # print(faceRects)
        for x, y, w, h in self.faceRects:
            cv2.rectangle(face_img, (x, y), (x + w, y + h), color=(255, 255, 0), thickness=1)
        cv2.imshow('img', face_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # 绘制logo
    def draw_logo(self, logo):
        face_rects = self.faceRects
        print(face_rects)
        face_img = self.faceImg
        cv2.imshow("img", face_img)
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
            print(face_img.shape)
            # print(small_logo.shape)
            # cv2.imshow("logo", small_logo)
            for row in range(small_logo_w):
                for col in range(small_logo_h):
                    face_img[face_y - small_logo_w + row, face_x + col] = small_logo[row, col]  # 注意：图像和数组维度位置的区别
        # cv2.imshow('smallLogo', smallLogo)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        cv2.imshow('img', face_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


faceDetect = FaceDetect()
faceDetect.face_detect()
logo = cv2.imread("./Image/logo.png")
faceDetect.draw_logo(logo)
