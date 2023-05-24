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

    def pose_landmarks(self, image):
        self.pose_results = self.pose.process(image)
        if self.pose_results.pose_landmarks:
            # 获取手的21个关键点
            pose_points = np.array(
                [pose_landmark.x, pose_landmark.y, pose_landmark.z]
                for pose_landmark in self.pose_results.pose_landmarks.landmark)
            # 设置关键点style
            posesype = mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 255), thickness=2)
            # 设置线条style
            lineesype = mp.solutions.drawing_utils.DrawingSpec(color=(255, 255, 0), thickness=3)
            # 手部关键点的连接
            pose_connections = mp.solutions.pose.POSE_CONNECTIONS
            mp.solutions.drawing_utils.draw_landmarks(image,
                                                      self.pose_results.pose_landmarks,
                                                      pose_connections,
                                                      posesype,
                                                      lineesype)
            for index, point in enumerate(pose_points):
                x, y = point[:2]
                cv2.putText(image, str(index), org=(x, y), fontFace=cv2.FONT_HE)
        return image