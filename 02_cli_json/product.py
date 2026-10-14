# 商品1種類を表すクラスです。
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_info(self):
        return f"{self.product_id}.{self.name} - {self.price}円"