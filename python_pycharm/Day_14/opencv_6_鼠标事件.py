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
# 初始化起始坐标
st_p = (0, 0)
ed_p = ()
# 打开背景
img = cv2.imread('back.jpg')
# 读取背景维度的元组
w, h, c = img.shape
# 对背景图片做个深拷贝
copyImg = copy.deepcopy(img)
# 定义窗口名
windowName = 'board'


# 定义鼠标时间回响
def call_back(event, x, y, flags, param):
    # 把需要修改的变量变为全局变量
    global st_p, ed_p, copyImg, img
    # 鼠标点击事件
    if event == cv2.EVENT_LBUTTONDOWN:
        # 定义鼠标按下的开始坐标位置
        st_p = (x, y)
    if event == cv2.EVENT_MOUSEMOVE:
        # 判断鼠标抬起事件 是否发生
        if st_p[0] > 0 and st_p[1] > 0:
            # 对每次移动事件的位置进行赋值
            ed_p = (x, y)
            # 将鼠标移动事件中图片进行初始化,回到鼠标移动事件之前,避免每一次鼠标移动事件都会在同一张背景上绘图
            img = copyImg.copy()
            # 显示背景图片
            cv2.imshow(windowName, img)
            # 在背景图片上绘制由开始坐标位置（st_p）和移动结束位置（ed_p)确定的线段
            cv2.line(img, st_p, ed_p, color=(255, 255, 0), thickness=2)
            # 展示绘图之后的背景图片
            cv2.imshow(windowName, img)

    if event == cv2.EVENT_LBUTTONUP:
        # 作为当鼠标抬起事件发生后,结束移动事件的绘图的判断条件
        st_p = (-1, -1)
        # 保留已绘制的图像,并赋值给之前已深拷贝的背景
        copyImg = img.copy()
    pass


# 定义鼠标绘画函数
def mouse_drawing():
    # 窗口命名
    cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
    # 根据背景图片的尺寸来设置窗口的大小
    cv2.resizeWindow(windowName, h, w)
    # 定义鼠标响应事件
    # 参数1 windowsName
    # 参数2 onMouse 函数
    # 参数3 para函数
    # 将函数注册在窗口（board）上  想要得到哪些信息 event x y flags params
    cv2.setMouseCallback(windowName, call_back, None)
    # 显示画布窗口
    cv2.imshow(windowName, img)
    # 参数为零表示一直显示
    cv2.waitKey(0)
    # 销毁所有窗口
    cv2.destroyAllWindows()
    pass


# 调用鼠标事件绘画函数
mouse_drawing()

