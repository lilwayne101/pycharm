import cv2
import numpy as np

# 定义棋盘
class Chessboard:
    # 棋盘
    board = None
    # 棋盘尺寸
    board_size = (800, 800, 3)



    # 创建棋盘
    @classmethod
    def create_board(cls):
        cls.board = np.full(cls.board_size, fill_value=(255, 255, 255), dtype=np.uint8)
        cls.full()
        cv2.imshow("chessboard", cls.board)
        key = cv2.waitKey(0)
        print(key)
        if key == ord('p'):
            cv2.destroyAllWindows()

    def line(self):
        pass

    # 填充棋盘颜色
    @classmethod
    def full(cls, size=(100, 100, 3)):
        full_size = np.full(size, fill_value=(0, 0, 0), dtype=np.uint8)
        for i in range(4):
            for j in range(4):
                cls.board[i * 2 * 100:i * 2 * 100 + 100, j * 2 * 100:j * 2 * 100 + 100, :] = full_size
                cls.board[(i * 2 + 1) * 100:(i * 2 + 1) * 100 + 100,
                (j * 2 + 1) * 100:(j * 2 + 1) * 100 + 100, :] = full_size






Chessboard.create_board()
