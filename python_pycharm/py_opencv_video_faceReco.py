import cv2
# 调用图片人脸识别的类
from py_opencv_faceReco import FaceDetect


# 定义一个视频人脸识别的类
class FaceRecoVideo:
    def __init__(self):
        # 定义成员变量
        self.facedetect = FaceDetect()

    # 定义视频人脸加logo类方法
    def logo_face_video(self):
        # 调用序列为0的摄像头,并返回cap
        cap = cv2.VideoCapture(0)
        # 判断摄像头打开执行循环
        while cap.isOpened():
            # 读取摄像头
            retval, image = cap.read()
            # 判断是否读取成功 未读取成功则跳出循环
            if not retval:
                print("can not read image")
                break
            # 调用作为成员变量的对象的方法 绘制人脸矩形
            self.facedetect.face_detect(image)
            # 读取并定义logo参数
            logo = cv2.imread("./Image/logo.png")
            # 调用作为成员变量的对象的方法 给人脸上方添加logo 并返回给face_img
            face_img = self.facedetect.draw_logo(logo)
            # 显示face_img
            cv2.imshow('image', face_img)
            key = cv2.waitKey(1)
            if key == ord('p'):
                break


face_reco_video = FaceRecoVideo()
face_reco_video.logo_face_video()

