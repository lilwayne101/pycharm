import cv2
import numpy as np


# 定义棋盘
class Board:
    # 棋盘
    white = []
    black = []
    times = 0
    scope = None
    board = None
    space = None
    full_size_2 = None
    full_size_1 = None
    judgment_board = np.zeros((30, 30), dtype=np.int32)
    # 棋盘尺寸
    board_size = (800, 800, 3)
    # 棋子落点
    point_list = []
    windows_name = "Gomoku"

    # 创建棋盘板
    @classmethod
    def create_board_plus(cls, w=1000, h=1000):
        cls.board = cv2.imread("back.png")
        cls.board = cls.board[:, :, :]
        cls.board = cv2.resize(cls.board, dsize=(w, h))
        cls.full()
        cv2.imshow(cls.windows_name, cls.board)


    # 刷新棋盘
    @classmethod
    def board_refresh(cls):
        cv2.imshow(cls.windows_name, cls.board)
        key = cv2.waitKey(0)
        # print(key)
        if key == ord('p'):
            cv2.destroyAllWindows()

    # 绘制棋盘格子
    @classmethod
    def full(cls):
        w, h, c = cls.board.shape
        cls.space = int(w / 20)
        cls.full_size_1 = np.full((1, h - cls.space, c), fill_value=(0, 0, 0), dtype=np.uint8)
        cls.full_size_2 = np.full((w - cls.space, 1, c), fill_value=(0, 0, 0), dtype=np.uint8)
        for i in range(1, 20):
            x = i * cls.space
            cls.board[x:x + 1, int(cls.space/2):-int(cls.space/2), :] = cls.full_size_1
            cls.board[int(cls.space/2):-int(cls.space/2), x:x + 1, :] = cls.full_size_2

    # 获取下棋点位
    @classmethod
    def get_point_list(cls):
        for row in range(2, 20):
            for col in range(2, 20):
                cls.point_list.append([row, col])

    # 黑棋
    @classmethod
    def place_piece(cls, point, color=(255, 255, 255)):
        cv2.circle(cls.board, point, int(cls.space / 2), color, -1)

    @classmethod
    # 鼠标响应事件
    def call_back_mouse(cls, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            # 定义鼠标按下的开始坐标位置
            st_p = (round((x / cls.space))*cls.space, round(y / cls.space)*cls.space)
            st_p_t = (round((x / cls.space)), round(y / cls.space))
            x_t = round((x / cls.space))
            y_t = round(y / cls.space)
            # print(st_p_t)
            if cls.times % 2 == 0 and cls.judgment_board[st_p_t] == 0 and x_t*y_t != 0:
                cls.times += 1
                cls.place_piece(st_p)
                cls.judgment_board[st_p_t] = 1
                cls.win(st_p_t)
            elif cls.times % 2 == 1 and cls.judgment_board[st_p_t] == 0 and x_t*y_t != 0:
                cls.times += 1
                cls.place_piece(st_p, color=(22, 22, 22))
                cls.judgment_board[st_p_t] = -1
                cls.win(st_p_t)
            cls.board_refresh()
        pass

    # 鼠标点击
    @classmethod
    def mouse_click(cls):
        cls.create_board_plus(800, 800)
        cv2.setMouseCallback(cls.windows_name, cls.call_back_mouse, None)
        cls.board_refresh()
        pass

    # 判断胜负
    @classmethod
    def win(cls, point):
        s1 = np.sum(cls.judgment_board[point[0]:point[0] + 5, point[1]])
        s2 = np.sum(cls.judgment_board[point[0] - 4:point[0] + 1, point[1]])
        s3 = np.sum(cls.judgment_board[point[0], point[1]: point[1] + 5])
        s4 = np.sum(cls.judgment_board[point[0], point[1] - 4: point[1]+1])
        s5 = sum([cls.judgment_board[point[0] - i, point[1] - i] for i in range(5)])
        s6 = sum([cls.judgment_board[point[0] - i, point[1] + i] for i in range(5)])
        s7 = sum([cls.judgment_board[point[0] + i, point[1] - i] for i in range(5)])
        s8 = sum([cls.judgment_board[point[0] + i, point[1] + i] for i in range(5)])
        if 5 in [s1, s2, s3, s4, s5, s6, s7, s8]:
            print("白胜")
            cv2.destroyAllWindows()
        if -5 in [s1, s2, s3, s4, s5, s6, s7, s8]:
            print("黑胜")
            cv2.destroyAllWindows()
        pass


Board.mouse_click()



