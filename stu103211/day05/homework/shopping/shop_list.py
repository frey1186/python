from user import file_manage
product_dict_file = "shopping/product_dict.txt"
user_file = "user/user.txt"
atm_log_file = "log/atm_log.txt"
from log import log


def list_shop_list(user):
    """
    列举用户购物车列表中的购物清单
    :param user: 登陆用户
    :return:
    """
    # fr = open(product_dict_file, "r")
    # product_list = json.load(fr)[user]
    # fr.close()
    product_dict = file_manage.file_read(product_dict_file)
    price = 0
    print("您老人家购物车里有：")
    print("-"*50)
    print("序号\t商品\t\t单价\t\t数量\t\t总价")
    if product_dict.get(user) and not product_dict.get(user) == [[]]:
        for i,p in enumerate(product_dict.get(user)):
            price += p[1]*p[2]
            print("%d\t%s\t%d元\t%d\t\t%d元" % (i,p[0],p[1],p[2],p[1]*p[2]))
        print("-"*50)
        print("总价：%d元" % price)
    return product_dict, price

def change_shop_list(user):
    """
    修改购物车中的商品数量
    :param user:
    :return:
    """
    product_dict = list_shop_list(user)[0]
    while True:
        input_str = input("请输入您需要修改的商品序号（Q：退出）：")
        if input_str.strip().lower() == "q":
            break
        elif input_str.strip().isdigit():
            if int(input_str) in range(len(product_dict[user])):
                input_count = input("修改数量（已选%d）：" % product_dict[user][int(input_str)][2])
                if input_count.strip().isdigit():
                    product_dict[user][int(input_str)][2] = int(input_count.strip())
                    if product_dict[user][int(input_str)][2] == 0:
                        product_dict[user].pop(int(input_str))
                    file_manage.file_write(product_dict, product_dict_file)
                elif input_count.strip() == "":
                    continue
                else:
                    print("输入错误。")
        else:
            print("输入错误。")

def del_shop_list(user):
    """
    删除购物车列表中的某项
    :param user:
    :return:
    """
    product_dict = list_shop_list(user)[0]
    while True:
        input_str = input("请输入您需要删除的商品序号（Q：退出）：")
        if input_str.strip().lower() == "q":
            break
        elif input_str.strip().isdigit():
            if int(input_str) in range(len(product_dict[user])):
                product_dict[user].pop(int(input_str))
                # fw = open(product_list_file, "w")
                # json.dump(product_list, fw)
                # fw.close()
                file_manage.file_write(product_dict, product_dict_file)
                break
            else:
                print("输入错误")
        else:
            print("输入错误。")




def maidan(user):
    """
    结账
    :param user:
    :return:
    """
    product_dict, price = list_shop_list(user)
    user_dict = file_manage.file_read(user_file)
    money_left = user_dict[user][5]
    print("你的信用卡号为:%s" % user_dict[user][2])

    print("你呀原有%s元,这次花了%s元." % (money_left, price))
    for i in range(3):
        input_pass = input("请输入你呀的支付密码:")
        if input_pass == user_dict[user][3]:
            if price > money_left:
                print("钱不够.")
                break
            else:
                money_left -= price
                user_dict[user][5] = money_left    #赋值回用户字典中
                file_manage.file_write(user_dict, user_file)  #写回原文件
                log.write_atm_log(user,"购物",price)
                product_dict.pop(user)
                file_manage.file_write(product_dict, product_dict_file)
                print("结账完成,剩下%s元." % money_left)    #打印结果
                break
        else:
            print("输入错误.")
    else:
        print("你呀错误次数太多了.")


def shop_list(user):
    """
    主函数
    """

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
                list_shop_list(user)
            elif int(input_str) == 2:
                change_shop_list(user)
            elif int(input_str) == 3:
                del_shop_list(user)
            elif int(input_str) == 4:
                maidan(user)
            else:
                print("滚.")
        else:
            print("滚。")



