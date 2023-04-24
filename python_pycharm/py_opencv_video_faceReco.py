import cv2
from py_opencv_faceReco import FaceDetect


class FaceRecoVideo:
    def __init__(self):
        self.facedetect = FaceDetect()

    def logo_face_video(self):
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            retval, image = cap.read()
            if not retval:
                print("can not read image")
                break

            self.facedetect.face_detect(image)
            logo = cv2.imread("./Image/logo.png")
            face_img = self.facedetect.draw_logo(logo)
            cv2.imshow('image', face_img)
            key = cv2.waitKey(1)
            if key == ord('p'):
                break

face_reco_video = FaceRecoVideo()
face_reco_video.logo_face_video()

