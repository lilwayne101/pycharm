import time

import copy

import random

import threading
from goods_stock import Goods
from file import File

lock = threading.Lock()


class User:
    user_list = ["小王", "小张", "小李", "小周", "小周"]

    def __init__(self):
        super().__init__()
        self.thread_list = [threading.Thread(target=self.purchase, name=name_user).start() for name_user in User.user_list]


    def purchase(self):
        while True:
            with lock:
                random.shuffle(Goods.data_goods)
                goods = Goods.data_goods[0]
                Goods.stock_fund += list(goods.values())[1] * Goods.profit
                print(f"{threading.currentThread().name}购买了1件{list(goods.values())[0]}"
                      f",库存余额入账{list(goods.values())[1] * Goods.profit}元,库存余额：{Goods.stock_fund}")
                del Goods.data_goods[0]
                time.sleep(0.5)

