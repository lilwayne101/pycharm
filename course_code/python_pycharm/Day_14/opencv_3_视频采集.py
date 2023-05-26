"""
    视频的本质：
    就是由一帧一帧的图像构成
    图像的显示和之前一致

    分析：
    1.视频采集（打开摄像头）
    2.读取图像信息
    3.显示图像信息
        显示
        等待按键按下
        释放窗口
"""
import cv2

# 参数：0 表示本地的摄像头序号
# 参数：地址 播放视频
cap = cv2.VideoCapture(0)
# 参数：retval 当前读取图像是否成功
# image 就是读取的图像
# 摄像打开是否成功
while cap.isOpened():
    retval, image = cap.read()
    if not retval:
        print("读取图像失败")
        break
    cv2.imshow('img', image)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
# 释放资源
cap.release()
# 销毁窗口
cv2.destroyAllWindows()

