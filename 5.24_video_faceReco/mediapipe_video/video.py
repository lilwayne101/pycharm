import cv2
import numpy as np
from hand import Hands
from pose import Pose
from face import Face


class Video:
    def __init__(self):
        self.image = None
        self.hands = Hands()
        self.pose = Pose()
        self.face = Face()

    def cap_video(self):
        video = cv2.VideoCapture(0)
        while video.isOpened():
            retval, self.image = video.read()
            if not retval:
                print("can not get image")
                break
            self.image = cv2.flip(self.image, 1)
            # 手部识别
            self.image = self.hands.add_image(self.image)
            # 肢体识别
            # self.image = self.pose.pose_landmarks(self.image)
            # 脸部识别
            # self.image = self.face.face_landmarks(self.image)
            self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
            cv2.imshow("MediaPipe Hand", self.image)
            if cv2.waitKey(1) == ord("q"):
                break
        video.release()
        cv2.destroyAllWindows()




video = Video()
video.cap_video()
