import mediapipe as mp
import cv2
import numpy as np
from guessing_game import Guessing


class Hands:
    def __init__(self):
        # 找到hands模块
        self.mp_hands = mp.solutions.hands
        # 视频流输入 (加载模块)
        self.hands = self.mp_hands.Hands(static_image_mode=False,
                                         max_num_hands=1,
                                         min_detection_confidence=0.5,
                                         min_tracking_confidence=0.5
                                         )
        self.hand_results = None
        # 初始化Guessing
        self.guessing = Guessing()
        self.hand_points = None

    def add_image(self, image):
        image_temp = self.hand_landmarks(image)
        return self.guessing.playing(image_temp, self.hand_points)

    def hand_landmarks(self, image):
        height, width = image.shape[:2]
        # 手部读取
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.hand_results = self.hands.process(image)
        if self.hand_results.multi_hand_landmarks:
            for i in range(len(self.hand_results.multi_hand_landmarks)):
                # 获取手的21个关键点
                self.hand_points = np.array(
                   [[hand_landmark.x, hand_landmark.y, hand_landmark.z]
                    for hand_landmark in self.hand_results.multi_hand_landmarks[i].landmark])
                # 设置关键点style
                handsype = mp.solutions.drawing_utils.DrawingSpec(color=(0, 0, 255), thickness=2)
                # 设置线条style
                lineesype = mp.solutions.drawing_utils.DrawingSpec(color=(255, 0, 0), thickness=1)
                # 手部关键点的连接
                hand_connections = mp.solutions.hands.HAND_CONNECTIONS
                mp.solutions.drawing_utils.draw_landmarks(image,
                                                          self.hand_results.multi_hand_landmarks[i],
                                                          hand_connections,
                                                          handsype,
                                                          lineesype)
                for idx, point in enumerate(self.hand_points):
                    x = int(point[0] * width)
                    y = int(point[1] * height)
                    cv2.putText(image,
                                str(idx),
                                (x, y),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=1,
                                color=(0, 255, 0),
                                thickness=1,
                                lineType=cv2.LINE_AA)

        return image


