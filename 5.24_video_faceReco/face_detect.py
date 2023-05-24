import mediapipe as mp
import cv2


class FaceDetect:
    def __init__(self):
        # 创建一个级联分类器
        self.classifier = cv2.CascadeClassifier()
        # 读取特征文件
        self.classifier.load(r"5.24_video_faceReco\classifier\haarcascade_frontalface_alt2.xml")
        self.coordinates = None

    def cap(self):
        cap = cv2.VideoCapture(1)
        while cap.isOpened():
            retval, image = cap.read()
            if not retval:
                print("can not get image")
                break
            self.coordinates = self.classifier.detectMultiScale(image)
            if image is None or image.size == 0:
                # print('图像读取失败!')
                continue
            else:
                cv2.imshow("cap", image)
            key = cv2.waitKey(1)
            if key == ord("q"):
                break
        cv2.destroyAllWindows()

    def get_point(self):
        for coord in self.coordinates:
            x, y, h, w = coord



