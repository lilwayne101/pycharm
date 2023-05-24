import cv2
import numpy as np
from PIL import Image


class VideoFace:
    def __init__(self):
        # 创建一个级联分类器
        self.classifier_1 = cv2.CascadeClassifier()
        self.classifier_2 = cv2.CascadeClassifier()
        self.classifier_3 = cv2.CascadeClassifier()
        # 读取特征文件
        # 人脸
        self.classifier_1.load(r"D:\pycharm_git_code_new\pycharm\5.24_video_faceReco\classifier\haarcascade_frontalface_alt2.xml")
        # 眼镜
        self.classifier_2.load(r"D:\pycharm_git_code_new\pycharm\5.24_video_faceReco\classifier\haarcascade_eye_tree_eyeglasses.xml")
        self.classifier_3.load(r"")
        # 人脸坐标
        self.face_coordinates = None
        # 眼睛坐标
        self.eyes_coordinates = None
        # 帽子
        self.hat = cv2.imread("pic/hat.jpg")
        # 眼镜
        self.glasses = cv2.imread("./pic/glasses.jpg")


    def cap_video(self):
        cap = cv2.VideoCapture(1)
        while cap.isOpened():
            retval, image = cap.read()
            if not retval:
                print("can not get image")
                break
            self.face_coordinates = self.classifier_1.detectMultiScale(image)
            self.eyes_coordinates = self.classifier_2.detectMultiScale(image)
            image = self.add_hat(image)
            try:
                image = self.add_glasses(image)
            except:
                pass
            if image is None or image.size == 0:
                # print('图像读取失败!')
                continue
            else:
                cv2.imshow("cap", image)
            key = cv2.waitKey(1)
            if key == ord("q"):
                break
        cv2.destroyAllWindows()

    def add_hat(self, image):
        for coord in self.face_coordinates:
            x, y, w, h = coord
            hat = cv2.resize(self.hat, (w, h//2))
            # image[y: y+h, x:x+w] = cv2.resize(cv2.resize(image[y: y+h, x:x+w], (15, 15)), (h, w))
            hat_h, hat_w, _ = hat.shape
            hat_y = y - hat_h
            img_hat = Image.fromarray(hat)
            img_image = Image.fromarray(image)
            mask_img = self.mask_make(img_hat)
            if hat_y < 0:
                img_image.paste(img_hat, (x, 0), mask=mask_img)
                # image[0: y, x:x + hat_w] = hat[0:y,:]
            else:
                img_image.paste(img_hat, (x, hat_y), mask=mask_img)
                # image[hat_y: y, x:x + hat_w] = hat
            return np.array(img_image)

    # 抠图的蒙板
    def mask_make(self, image, threshold=200):
        grayscale_image = image.convert("L")
        mask = grayscale_image.point(lambda x: 0 if x < threshold else 255)
        return Image.fromarray(cv2.bitwise_not(np.array(mask)))

    def add_glasses(self, image):
        for coord in self.eyes_coordinates:
            x, y, h, w = coord
            x = x - w
            _, _, w_1, h_1 = self.face_coordinates[0]
            glasses_1 = cv2.resize(self.glasses, (w_1, h_1//3))
            image = Image.fromarray(image)
            glasses = Image.fromarray(glasses_1)
            mask = self.mask_make(glasses)
            if len(self.eyes_coordinates) % 2 == 0:
                image.paste(glasses, (x, y), mask=mask)
            return np.array(image)


video_face = VideoFace()
video_face.cap_video()