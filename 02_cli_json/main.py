from cart import Cart
from product_storage import load_products

def cart_info(cart,sum=True):
    if len(cart.items) == 0:
        print("カートは空です")
    else:
        index = 1
        for item in cart.items:
            print(f"{index}.{item.name} - {item.price}円")
            index += 1
    if sum:
        print(f"商品数:{len(cart.items)}点 / 合計: {cart.get_total()}円")

def main():
    products = load_products()
    cart = Cart()
    while True:
        print("===メニュー===")
        print("1:商品一覧")
        print("2:カートに追加")
        print("3:カート一覧")
        print("4:カートから削除")
        print("0:終了")
        print("=============")
        choice = input("コマンドを入力：")
        if choice == "1":
            print("--商品一覧--")
            for product in products:
                print(f"{product.get_info()}")
        elif choice == "2":
            print("--カートに追加--")
            add_flg = False
            try:
                selected = int(input("商品番号を入力："))
            except ValueError:
                print("エラー：整数を入力してください")
                continue
            for product in products:
                if selected == product.product_id:
                    cart.add_product(product)
                    add_flg = True
                    break
            if add_flg:
                cart_info(cart)
            else:
                print("エラー：商品が見つかりませんでした")
        elif choice == "3":
            print("--カート一覧--")
            cart_info(cart)
        elif choice == "4":
            print("--カートから削除--")
            if len(cart.items) == 0:
                print("カートは空です")
            else:
                cart_info(cart,False)
                try:
                    selected = int(input("カート番号を入力："))
                except ValueError:
                    print("エラー：整数を入力してください")
                    continue
                if selected != 0 and selected <= len(cart.items):
                    cart.remove_product(selected-1)
                    cart_info(cart)
                else:
                    print("エラー：存在しないカート番号です")
        elif choice == "0":
            print("--終了します--")
            break
        else:
            print("エラー：無効なコマンドです")

if __name__ == "__main__":
    main()
