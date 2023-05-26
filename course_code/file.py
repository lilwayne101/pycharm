import time
import threading
import os
import json
from goods_stock import Goods


class File:

    def __init__(self):
        self.sync = threading.Thread(target=self.synchronizer).start()

    @staticmethod
    def path_find():
        temp_path = os.getcwd()
        file_name = "goods_stock"
        file_path = os.path.join(temp_path, file_name)
        if not os.path.isdir(file_path):
            os.mkdir(file_path)
        return file_path

    # 写入仓库文件
    def write_goods_stock(self, data):
        path = self.path_find()
        if not os.path.isdir(path):
            os.mkdir(path)
        with open(path+"//stock_goods.txt", "w+") as file_stock:
            file_stock.write(self.data_dispose(data))

    # 数据处理
    def data_dispose(self, data):
        if not self.is_json(data):
            data = json.dumps(data)
        return data

    @staticmethod
    def is_json(data):
        try:
            data = json.loads(data)
        except Exception as e:
            return False
        return True

    # 读出仓库文件
    def read_good_stock(self):
        path = self.path_find()
        with open(path, "r") as file_stock:
            data = file_stock.read()
            return data

    def synchronizer(self):
        while True:
            data = Goods.data_goods
            self.write_goods_stock(data)
            time.sleep(1)


