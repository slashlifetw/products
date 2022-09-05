products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    # p = []
    # p.append(name) # 小清單
    # p.append(price) # 小清單
    # 上面三行等於下面一行
    # p = [name, price]
    # products.append(p) # 大清單
    # 上面兩行可以合併成下面一行
    products.append([name, price])
print(products)

for p in products:
    print(p[0], '的價格是', p[1])