# 商品オブジェクトを受け取り、カートの中身を管理します。
class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]
            return True
        else:
            return False

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total