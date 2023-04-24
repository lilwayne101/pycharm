"""
    简易画板
    鼠标
    位置 事件（按下去  弹起来   移动）

"""
import copy

import cv2


# 回调函数
"""
    绘制直线
    确定起始点，终点
    鼠标弹起来之后，进行显示（绘制）
    
    作业：绘制线，矩形，圆
    拓展作业：1.看见绘制过程
            2.按下不同的键绘制不同的图形  l(线) r(矩阵) c(圆)
"""
st_p = ()
mo_p = ()
ed_p = ()
img = cv2.imread('back.jpg')
w, h, c = img.shape
copyImg = copy.deepcopy(img)
print(img.shape)
windowName = 'board'


def call_back(event, x, y, flags, param):
    global st_p, ed_p, img
    if event == cv2.EVENT_LBUTTONDOWN:
        st_p = (x, y)
        # print(f"{event}： x:{x}   y:{y}")
    if event == cv2.EVENT_MOUSEMOVE:
        if st_p[0] > 0 and st_p[1] > 0:
        # print(f"{event}： x:{x}   y:{y}")
        # img[y, x] = (255, 255, 0)
            ed_p = (x, y)
            img = copyImg.copy()
            cv2.imshow(windowName, img)
            cv2.line(img, st_p, ed_p, color=(255, 255, 0), thickness=2)
            cv2.imshow(windowName, img)

    if event == cv2.EVENT_LBUTTONUP:
        st_p = (-1, -1)
        img = copyImg.copy()
        # ed_p = (x, y)
        # print(f"{event}： x:{x}   y:{y}")
        # img[y, x] = (255, 255, 0)
        # cv2.line(img, st_p, ed_p, color=(255, 255, 0), thickness=2)
        # cv2.imshow(windowName, img)
    pass


def mouse_drawing():
    cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(windowName, h, w)
    # 参数1 windowsName
    # 参数2 onMouse 函数
    # 参数3 para函数
    # 将函数注册在窗口（board）上  想要得到哪些信息 event x y flags params
    cv2.setMouseCallback(windowName, call_back, None)
    cv2.imshow(windowName, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass


mouse_drawing()

