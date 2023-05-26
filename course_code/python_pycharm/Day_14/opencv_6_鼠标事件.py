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


class MouseDraw:
    def __init__(self):
        # 初始化起始坐标
        self.st_p = (0, 0)
        self.ed_p = ()
        # 打开背景
        self.img = cv2.imread('back.jpg')
        # 读取背景维度的元组
        self.w, self.h, self.c = self.img.shape
        # 对背景图片做个深拷贝
        self.copy_img = copy.deepcopy(self.img)
        # 定义窗口名
        self.windowName = 'board'


    # 定义鼠标时间回响
    def call_back_draw_line(self, event, x, y, flags, param):
        # 把需要修改的变量变为全局变量
        window_name = self.windowName
        st_p = self.st_p
        ed_p = self.ed_p
        copy_img = self.copy_img
        img = self.img
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
                img = copy_img.copy()
                # 显示背景图片
                cv2.imshow(window_name, img)
                # 在背景图片上绘制由开始坐标位置（st_p）和移动结束位置（ed_p)确定的线段
                cv2.line(img, st_p, ed_p, color=(255, 255, 0), thickness=2)
                # 展示绘图之后的背景图片
                cv2.imshow(window_name, img)

        if event == cv2.EVENT_LBUTTONUP:
            # 作为当鼠标抬起事件发生后,结束移动事件的绘图的判断条件
            st_p = (-1, -1)
            # 保留已绘制的图像,并赋值给之前已深拷贝的背景
            copy_img = img.copy()
        pass


    def call_back_draw_rectangle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.st_p = (x, y)
        if event == cv2.EVENT_MOUSEMOVE:
            if self.ed_p[0] == -1 and self.ed_p[1] == -1:
                self.ed_p = (x, y)
                self.img = self.copy_img
                cv2.imshow(self.windowName, self.img)
                cv2.rectangle(self.img, self.st_p, self.ed_p, color=(0, 255, 255), thickness=-1)
                cv2.imshow(self.windowName,self.img)
        if event == cv2.EVENT_LBUTTONUP:
            self.ed_p = (-1, -1)
            self.copy_img = self.img




        pass


    # 定义鼠标绘画函数
    def mouse_drawing_line(self):
        # 窗口命名
        cv2.namedWindow(self.windowName, cv2.WINDOW_NORMAL)
        # 根据背景图片的尺寸来设置窗口的大小
        cv2.resizeWindow(self.windowName, self.h, self.w)
        # 定义鼠标响应事件
        # 参数1 windowsName
        # 参数2 onMouse 函数
        # 参数3 para函数
        # 将函数注册在窗口（board）上  想要得到哪些信息 event x y flags params
        cv2.setMouseCallback(self.windowName, self.call_back_draw_line, None)
        # 显示画布窗口
        cv2.imshow(self.windowName, self.img)
        # 参数为零表示一直显示
        cv2.waitKey(0)
        # 销毁所有窗口
        cv2.destroyAllWindows()
        pass

    # 绘制矩形
    def mouse_drawing_rectangle(self):
        # 窗口命名
        cv2.namedWindow(self.windowName, cv2.WINDOW_NORMAL)
        # 窗口大小
        cv2.resizeWindow(self.windowName, self.h, self.w)
        # 定义鼠标响应事件
        cv2.setMouseCallback(self.windowName, self.call_back_draw_rectangle, None)
        cv2.imshow(self.windowName, self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


mouse_draw = MouseDraw()

# 调用鼠标事件绘画矩形方法
mouse_draw.mouse_drawing_rectangle()
# 调用鼠标事件绘画方法
mouse_draw.mouse_drawing_line()

