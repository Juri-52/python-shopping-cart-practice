# 第2段階：CLIの商品カタログをJSONから読み込む

第1段階のカート操作はそのまま使い、商品の準備方法だけを変更します。10商品の名前・価格をPythonコードに直接書かず、配布された `products.json` から読み込みます。

## すでに作成した部分

第1段階で完成した `product.py`、`cart.py`、`main.py` をこのフォルダーにコピーしてください。配布されたひな形は、完成した自分のファイルで置き換えます。

- `product.py` と `cart.py` は変更しません。
- メニュー、追加、削除、一覧表示、入力チェックも再利用します。
- 第1段階のcatalog.pyの代わりに、同じ10商品が入ったproducts.jsonを読み込みます。

## 新しく作る部分

`product_storage.py` の読み込み関数を完成させ、その後に `main.py` の商品準備だけを変更します。

## 3. 商品データの読み込み

`product_storage.py` の `load_products()` を完成させます。

1. `open("products.json", "r", encoding="utf-8")` でファイルを開く。
2. JSONを読み込み、辞書のリストに変換する。
3. 辞書の `product_id`、`name`、`price` を使ってProductを作る。
4. 10個のProductが入ったリストを返す。

JSONの形式：

```json
[
  {"product_id": 1, "name": "ノート", "price": 200},
  {"product_id": 2, "name": "ボールペン", "price": 150}
]
```

上記は形式を説明するための抜粋です。配布ファイルには10商品が入っています。配布された正しい形式のファイルを前提とし、複雑なファイル検証は必要ありません。

## pandasを使ってもよい

JSONの読み込みには、標準ライブラリのjsonの代わりに **pandasを使っても構いません**。使い慣れた方法を選んでください。pandasは必須ではありません。

pandasを使う場合は、`pd.read_json("products.json")` で読み込めます。読み込み結果はDataFrameなので、各行のデータからProductを作成してください。どちらの方法でも、`load_products()` の戻り値は **Productオブジェクトのリスト** にします。DataFrameをそのまま返す形にはしません。

pandasが入っていない環境では、次のコマンドでインストールできます。

```text
python3 -m pip install pandas
```

環境によっては `python3` を `python` に読み替えてください。pandasを使った場合は、提出時に必要なライブラリとしてREADMEに記載してください。

## main.pyの変更箇所

1. `from catalog import PRODUCTS` を削除し、`load_products` を `product_storage` からインポートする。
2. PRODUCTSの辞書からProductを作っていた部分を、`load_products()` の呼び出しに置き換える。
3. `main.py` 内でProductを直接作らなくなったら、Productのインポートも削除する。

**メニュー全体を書き直す必要はありません。** 商品のリストが準備できれば、以降は第1段階と同じです。

カタログは読み込み専用です。JSONへカートを書き込む処理は作りません。

## 実行と確認

このフォルダーで `python3 main.py` を実行します。

- JSON内の10商品が表示される。
- ノート2点とボールペン1点で550円になる。全10商品を1点ずつ追加すると4850円になる。
- 追加・削除してもJSONの内容が変わらない。
- 再起動するとカートは空になる。
