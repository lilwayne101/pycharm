import mediapipe as mp
import cv2
import numpy as np


class Face:
    def __init__(self):
        # 找到pose模块
        self.mp_face = mp.solutions.face_mesh
        # 加载模块
        self.face = self.mp_face.FaceMesh(static_image_mode=False,
                                          min_detection_confidence=0.5,
                                          min_tracking_confidence=0.5
                                          )
        # pose读取
        self.face_results = None
        self.face_points = None

    def face_landmarks(self, image):
        height, width = image.shape[:2]
        self.face_results = self.face.process(image)
        landmark = self.face_results.multi_face_landmarks.landmark
        if self.face_results.multi_face_landmarks:
            # 获取脸部关键点
            face_points = np.array(
                [face_landmark.x, face_landmark.y, face_landmark.z]
                for face_landmark in self.face_results.multi_face_landmarks)
            # 设置关键点style
            facesype = mp.solutions.drawing_utils.DrawingSpec(color=(0, 255, 255), thickness=2)
            # 设置线条style
            lineesype = mp.solutions.drawing_utils.DrawingSpec(color=(255, 255, 0), thickness=3)
            # 手部关键点的连接
            face_connections = mp.solutions.face_mesh_connections
            mp.solutions.drawing_utils.draw_landmarks(image,
                                                      self.face_results.multi_face_landmarks,
                                                      face_connections,
                                                      facesype,
                                                      lineesype)
            for idx, point in enumerate(self.face_points):
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