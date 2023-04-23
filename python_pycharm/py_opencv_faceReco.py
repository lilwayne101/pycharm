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
        self.faceImg = cv2.imread(r".\Image\LENIN2.jpg")
        self.classifier = cv2.CascadeClassifier()
        # 加载特征文件
        self.classifier.load(r"D:\anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml")

    # 人脸矩形区域绘制
    def face_detect(self):
        faceImg = copy.deepcopy(self.faceImg)
        classifier = self.classifier
        # 识别图像中的人脸  返回矩形区域  使用列表进行存储
        faceRects = classifier.detectMultiScale(faceImg)
        # print(faceImg)
        # [[76 31 51 51]]   x y w h
        # print(faceRects)
        # for x, y, w, h in faceRects:
            cv2.rectangle(faceImg, (x, y), (x + w, y + h), color=(255, 255, 0), thickness=1)
        cv2.imshow('img', faceImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    # 绘制logo
    def draw_logo(self, logo):
        faceImg = copy.deepcopy(self.faceImg)
        faceRects = self.classifier.detectMultiScale(faceImg)
        cv2.imshow("img", faceImg)
        # 计算图像的缩放比例
        ratio = logo.shape[0] / logo.shape[1]
        faceX = faceRects[0][0]
        faceY = faceRects[0][1]
        faceW = faceRects[0][2]
        faceH = int(faceRects[0][3] * ratio)
        # 因为图像比较大,需要缩放
        smallLogo = cv2.resize(logo, dsize=(faceW, faceH))
        smallLogoH, smallLogoW = smallLogo.shape[:2]
        for row in range(smallLogoH):
            for col in range(smallLogoW):
                faceImg[col, row] = smallLogo[col ,row]
                break
            break
        cv2.imshow('smallLogo', smallLogo)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


faceDetect = FaceDetect()
faceDetect.face_detect()
logo = cv2.imread("./Image/logo.png")
faceDetect.draw_logo(logo)
