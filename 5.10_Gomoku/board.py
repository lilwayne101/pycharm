import cv2
import numpy as np


# 定义棋盘
class Board:
    # 棋盘
    board = None
    space = None
    full_size_2 = None
    full_size_1 = None
    # 棋盘尺寸
    board_size = (800, 800, 3)
    # 棋子落点
    point_list = []
    windows_name = "五子棋"

    # 创建棋盘板
    @classmethod
    def create_board_plus(cls, w=1000, h=1000):
        cls.board = cv2.imread("back.png")
        cls.board = cv2.resize(cls.board, dsize=(w, h))
        cls.full()
        cv2.imshow("chessboard", cls.board)




    # 创建棋盘
    @classmethod
    def create_board(cls):
        cls.create_board_plus(800, 800)


    # 刷新棋盘
    @classmethod
    def board_refresh(cls):
        cv2.imshow("chessboard", cls.board)
        key = cv2.waitKey(0)
        print(key)
        if key == ord('p'):
            cv2.destroyAllWindows()

    def line(self):
        pass

    # 绘制棋盘格子
    @classmethod
    def full(cls):
        w, h, c = cls.board.shape
        cls.space = int(w / 20)
        cls.full_size_1 = np.full((1, h - cls.space, c), fill_value=(0, 0, 0), dtype=np.uint8)
        cls.full_size_2 = np.full((w - cls.space, 1, c), fill_value=(0, 0, 0), dtype=np.uint8)
        for i in range(1, 20):
            x = i * cls.space
            cls.board[x:x + 1, int(cls.space/2):int(-cls.space/2), :] = cls.full_size_1
            cls.board[int(cls.space/2):int(-cls.space/2), x:x + 1, :] = cls.full_size_2

    # 获取下棋点位
    @classmethod
    def get_point_list(cls):
        for row in range(21):
            for col in range(21):
                cls.point_list.append([row * cls.space - 1, col * cls.space - 1])

    # 黑棋
    @classmethod
    def place_piece(cls, point, color=(255, 255, 255)):
        cv2.circle(cls.board, point, int(cls.space / 2), color, -1)

    @classmethod
    # 鼠标响应事件
    def call_back_mouse(cls, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(1)
            # 定义鼠标按下的开始坐标位置
            st_p = (x, y)
            cls.find_point(st_p)
            cls.board_refresh()
        pass

    # 鼠标点击
    @classmethod
    def mouse_click(cls):
        cls.create_board()
        print(1)
        cv2.setMouseCallback(Board.windows_name, cls.call_back_mouse)
        print(2)
        cls.board_refresh()
        pass

    # 找落点
    @classmethod
    def find_point(cls, st_p):
        print(1)
        for point in cls.point_list:
            scope = []
            for j in range(cls.space):
                scope.append([[point[0] - int(cls.space / 2) + i, point[1] - int(cls.space / 2)]
                              for i in range(Board.space)])
                print(scope)
            if st_p in scope:
                cls.place_piece(point)


Board.mouse_click()


