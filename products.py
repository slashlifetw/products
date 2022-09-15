products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    price = int(price)
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


with open('products.csv', 'w') as f:
    f.write('商品, 價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')
        #第7行把price轉換成整數，做加法時要使用相同格式，所以要把整數轉乘Stringa,str()