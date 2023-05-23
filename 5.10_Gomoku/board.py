import copy
import random

import cv2
import numpy as np
from PIL import ImageDraw, ImageFont, Image


# 定义棋盘
class Board:
    # 棋盘
    b_p_r = None
    white_count = 0
    black_count = 0
    m = 0
    chess_count = {"白棋": 0, "黑棋": 1}
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
    board_temp = None
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
            cls.board[x:x + 2, int(cls.space/2):-int(cls.space/2), :] = cls.full_size_1
            cls.board[int(cls.space/2):-int(cls.space/2), x:x + 2, :] = cls.full_size_2

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
            list_t = [1, -1, 0]
            if cls.judgment_board[st_p_t] == 0 and x_t*y_t * (st_p_t[0] - 20) *(st_p_t[1] - 20)!= 0:
                cls.place_piece(st_p)

                cls.acount(0)
                cls.judgment_board[st_p_t] = 1
                cls.win(st_p_t)
                k = 0
                if cls.m == 0:
                    while True:
                        b_p_t = (x_t + list_t[random.randint(0, 1)], y_t + list_t[random.randint(0, 1)])
                        cls.b_p_r = b_p_t
                        if b_p_t[0] * b_p_t[1] * (b_p_t[0] - 20) * (b_p_t[1] - 20) != 0:
                            break
                    b_p = (b_p_t[0] * cls.space, b_p_t[1] * cls.space)
                    cls.place_piece(b_p, color=(22, 22, 22))
                    cls.acount(1)
                    cls.judgment_board[b_p_t] = -1
                    cls.win(b_p_t)
                    cls.m = 1
                else:
                    kb = 0

                    while k == 0 and kb <= 20:

                        b_p_t = (cls.b_p_r[0] + random.choice(list_t), cls.b_p_r[1] + random.choice(list_t))
                        b_p = (b_p_t[0] * cls.space, b_p_t[1] * cls.space)

                        jdment = sum([cls.judgment_board[b_p_t[0] - 1, b_p_t[1] + i] for i in range(-1, 2)
                                      if cls.judgment_board[b_p_t[0] - 1, b_p_t[1] + i] == -1])
                        jdment += sum([cls.judgment_board[b_p_t[0], b_p_t[1] + i] for i in range(-1, 2)
                                       if cls.judgment_board[b_p_t[0], b_p_t[1] + i] == -1])
                        jdment += sum([cls.judgment_board[b_p_t[0] + 1, b_p_t[1] + i] for i in range(-1, 2)
                                       if cls.judgment_board[b_p_t[0] + 1, b_p_t[1] + i] == -1])
                        kb += 1

                        if cls.judgment_board[b_p_t] == 0 and jdment <= 1 and b_p_t[0] * b_p_t[1] * (b_p_t[0] - 20) * (
                                b_p_t[1] - 20) != 0:
                            if k == 21:
                                while cls.judgment_board[b_p_t] != 0 and b_p_t[0] * b_p_t[1] * (b_p_t[0] - 20) * (
                                        b_p_t[1] - 20) != 0:
                                    b_p_t = (random.randint(1, 19), random.randint(1, 19))
                                    b_p = (b_p_t[0] * cls.space, b_p_t[1] * cls.space)
                            cls.place_piece(b_p, color=(22, 22, 22))

                            cls.acount(1)
                            cls.judgment_board[b_p_t] = -1
                            cls.b_p_r = b_p_t
                            cls.win(b_p_t)

                            k = 1
                            kb = 1
            # cls.board_refresh()
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
        for k in range(5):
            s1 = np.sum(cls.judgment_board[point[0] - k:point[0] - k + 5, point[1]])
            s3 = np.sum(cls.judgment_board[point[0], point[1] - k: point[1] - k + 5])
            s5 = sum([cls.judgment_board[point[0] + k - i, point[1] + k - i] for i in range(5)])
            s6 = sum([cls.judgment_board[point[0] - i + k, point[1] + i - k] for i in range(5)])
            if 5 in [s1, s3, s5, s6, ]:
                print("白胜")
                cv2.destroyAllWindows()
            if -5 in [s1, s3, s5, s6]:
                print("黑胜")
                cv2.destroyAllWindows()
        pass

    # 黑棋自走
    @classmethod
    def choice_black(cls):
        pass

    # 已下棋子数
    @classmethod
    def acount(cls, k):
        # 白棋为0 黑为1
        cls.board_temp = copy.deepcopy(cls.board)
        board = cls.board_temp
        # print(type(board))
        img = Image.fromarray(board)
        # print(img)
        # img = np.array(cls.board)
        # img = Image.fromarray(img)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(r"G:\AaTangZiYingHua\AaTangZiYingHua\AaTangZiYingHua-2.ttf", size=15)
        draw.text((0, 0), text=f"{list(cls.chess_count.keys())[0]}: {list(cls.chess_count.values())[0]}",
                  fill=(0, 0, 0), font=font)
        draw.text((740, 0), text=f"{list(cls.chess_count.keys())[1]}: {list(cls.chess_count.values())[1]}",
                  fill=(0, 0, 0), font=font)
        img = np.array(img)
        # print(type(img))
        # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        board = np.array(img)
        # cls.board = board
        cls.chess_count[list(cls.chess_count.keys())[k]] += 1
        cv2.imshow(cls.windows_name, board)
        # cls.board = Image.fromarray(img)

Board.mouse_click()


