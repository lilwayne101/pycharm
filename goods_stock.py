import threading
import time
import random


class Goods:
    data_goods = []
    stock_fund = 50000
    data_goods_brand = {"小米手机": 2000, "华为手机": 3000, "苹果手机": 4000,
                        "一加手机": 2500, "锤子手机": 1900, "诺基亚手机": 500}
    profit = 1.3

    def __init__(self):
        self.flow_thread = threading.Thread(target=self.flow_goods_stock).start()

    def create_goods_stock(self, num=50):
        data_goods_stock = [self.add_goods_one() for i in range(num)]
        Goods.data_goods = data_goods_stock
        return data_goods_stock

    def flow_goods_stock(self):
        while True:
            self.goods_storage()
            self.flow_stock_fund()
            time.sleep(1)

    # 新商品入库
    def goods_storage(self):
        temp_goods_list = [self.add_goods_one() for i in range(random.randint(1, 5))]
        Goods.data_goods.extend(temp_goods_list)
        return temp_goods_list

    # 库存资金进出
    def flow_stock_fund(self):
        temp_goods_list = self.goods_storage()
        for goods in temp_goods_list:
            if (Goods.stock_fund - list(goods.values())[1]) < 0:
                return print(f"仓库资金不足,无法购买！")
            Goods.stock_fund -= list(goods.values())[1]
            print(f"成功入库一台{list(goods.keys())[0]}，库存资金扣除{list(goods.values())[1]}")
            print(f"目前仓库资金池为：{Goods.stock_fund}")

    @classmethod
    def add_goods_one(cls):
        random.seed()
        name = random.choice(list(cls.data_goods_brand.keys()))
        return {"商品": name, "价格": cls.data_goods_brand[name]}

    @classmethod
    def show_goods_stock(cls):
        print(cls.data_goods)

    def run(self):
        self.flow_thread.start()

