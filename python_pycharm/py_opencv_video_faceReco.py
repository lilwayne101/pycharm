import cv2
from py_opencv_faceReco import FaceDetect


class FaceReco_video:
    def __init__(self):
      self.facedetect = FaceDetect()
    def logo_face_video(self):
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            retval, image = cap.read()
            if not retval:
                print("can not read image")
                break
            cv2.imshow('image', image)
            self.facedetect.face_detect()
            logo = cv2.imread("./Image/logo.png")
            self.facedetect.draw_logo(loge)
            key =  cv2.waitKey(1)
            if key == ord('p'):
                break


