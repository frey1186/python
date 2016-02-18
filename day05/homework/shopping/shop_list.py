import json
from shopping.shopping import product_list_file



def list_shop_list(product_list_file):
    fr = open(product_list_file, "r")
    product_list = json.load(fr)
    fr.close()
    price = 0
    print("您老人家购物车里有：")
    print("-"*50)
    print("序号\t商品\t\t单价\t\t数量\t\t总价")
    for i,p in enumerate(product_list):
        price += p[1]*p[2]
        print("%d\t%s\t%d元\t%d\t\t%d元" % (i,p[0],p[1],p[2],p[1]*p[2]))
    print("-"*50)
    print("总价：%d元" % price)
    return product_list

def change_shop_list(product_list_file):
    product_list = list_shop_list(product_list_file)
    while True:
        input_str = input("请输入您需要修改的商品序号（Q：退出）：")
        if input_str.strip().lower() == "q":
            break
        elif input_str.strip().isdigit():
            if int(input_str) in range(len(product_list)):
                input_count = input("修改数量（已选%d）：" % product_list[int(input_str)][2])
                if input_count.strip().isdigit():
                    product_list[int(input_str)][2] = int(input_count.strip())
                    fw = open(product_list_file, "w")
                    json.dump(product_list, fw)
                    fw.close()
                    #return product_list
                elif input_count.strip() == "":
                    continue
                else:
                    print("输入错误。")
        else:
            print("输入错误。")
def del_shop_list(product_list_file):
    product_list = list_shop_list(product_list_file)
    while True:
        input_str = input("请输入您需要删除的商品序号（Q：退出）：")
        if input_str.strip().lower() == "q":
            break
        elif input_str.strip().isdigit():
            if int(input_str) in range(len(product_list)):
                product_list.pop(int(input_str))
                fw = open(product_list_file, "w")
                json.dump(product_list, fw)
                fw.close()
                break
            else:
                print("输入错误")
        else:
            print("输入错误。")

def maidan(product_list_file):
    product_list = list_shop_list(product_list_file)





    pass




def shop_list():

    while True:
        print("""
    1. 查看购物列表
    2. 修改购物数量
    3. 删除购物商品
    4. 哥要结算
    """)
        input_str = input("输入您的选择：（Q：退出）")
        if input_str.strip().lower() == "q":
            print("退出。")
            break
        elif input_str.strip().isdigit():
            if int(input_str) == 1:
                list_shop_list(product_list_file)
            elif int(input_str) == 2:
                change_shop_list(product_list_file)
            elif int(input_str) == 3:
                del_shop_list(product_list_file)
            elif int(input_str) == 4:
                maidan(product_list_file)
            else:
                print("滚.")
        else:
            print("滚。")




if __name__ == '__main__':
    shop_list()