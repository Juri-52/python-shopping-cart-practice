import pandas as pd
from product import Product


def load_products():
    df = pd.read_json("products.json")
    products = []
    for id, name, price in zip(df["product_id"], df["name"], df["price"]):
        product = Product(id, name, price)
        products.append(product)
    return products