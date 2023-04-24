"""
    人脸识别

    怎样才算一张脸：
    眼睛,眉毛，鼻子，嘴巴...

    级联分类器

"""
import cv2

class FaceDetect:
    def __init__(self):
        pass

    def face_detect(self):
        # 创建一个级联分类器,用来识别人脸
        classfier = cv2.CascadeClassifier()
        # 加载特征文件
        classfier.load()