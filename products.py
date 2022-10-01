import os # operating system

# 讀取檔案
def read_file(filename):
    products = [] 
    with open(filename, 'r') as f:
        for line in f:
            if '商品,價格' in line:
                continue
                # continue意思是跳下一個迴圈 
            # s = line.strip().split(',')
            # name = s[0]
            # price = s[1]
            # 上面三行進化合併如下行
            name, price = line.strip().split(',')
            # split=切割，我們是用','去區分'商品'及'價格' 所以用','下去當切割線
            # print(s)
            products.append([name, price])
    return products
    
# 讓使用者輸入
def user_input(products):
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
    return products

# 印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')
            #第7行把price轉換成整數，做加法時要使用相同格式，所以要把整數轉乘Stringa,str()

def main():
    filename = 'products.csv'
    if os.path.isfile(filename): # 檢查檔案在不再
        print('yeah! 找到檔案了!')
        products = read_file(filename)
    else:
        print('找不到檔案.....')
    products = user_input(products)
    print_products(products)
    write_file(filename, products)

main()

# 把程式改寫成function在程式裡有專有名詞「refector(程式重構)」