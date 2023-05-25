import mediapipe as mp
import cv2
import numpy as np


class Pose:
    def __init__(self):
        # 找到pose模块
        self.mp_pose = mp.solutions.pose
        # 加载模块
        self.pose = self.mp_pose.Pose(static_image_mode=False,
                                      min_detection_confidence=0.5,
                                      min_tracking_confidence=0.5
                                      )
        # pose读取
        self.pose_results = None
        self.pose_points = None

    def pose_landmarks(self, image):
        height, width = image.shape[:2]
        self.pose_results = self.pose.process(image)
        if self.pose_results.pose_landmarks:
            # 获取肢体关键点
            self.pose_points = np.array(
                [pose_landmark.x, pose_landmark.y, pose_landmark.z]
                for pose_landmark in self.pose_results.pose_landmarks.landmark)
            # 设置关键点style
            posesype = mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 255), thickness=2)
            # 设置线条style
            lineesype = mp.solutions.drawing_utils.DrawingSpec(color=(255, 255, 0), thickness=3)
            # 肢体关键点的连接
            pose_connections = mp.solutions.pose.POSE_CONNECTIONS
            mp.solutions.drawing_utils.draw_landmarks(image,
                                                      self.pose_results.pose_landmarks,
                                                      pose_connections,
                                                      posesype,
                                                      lineesype)
            for idx, point in enumerate(self.pose_points):
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