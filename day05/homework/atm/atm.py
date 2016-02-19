from shopping import shopping, shop_list
from user import file_manage
from log import log
import time,datetime
user_file = "user/user.txt"
atm_log_file = "log/atm_log.txt"



def shop_with_card(user):
    """

    :param user: 登陆用户
    :return: 购物
    """
    shopping.shopping(user)
    shop_list.shop_list(user)

def cash_out(user):
    """

    :param user: 登陆的用户
    :return: 取现
    """
    user_dict = file_manage.file_read(user_file)
    money_out_max = user_dict[user][5] * 0.5
    input_num = input("输入你呀要取得钱数目,穷光蛋:")
    if input_num.strip().isdigit():
        if int(input_num) > 0 and int(input_num) < money_out_max:
            for i in range(3):
                input_pass = input("输入你呀的在支付密码:")
                if input_pass == user_dict[user][3]:
                    user_dict[user][5] = money_out_max - int(input_num)
                    file_manage.file_write(user_dict, user_file)
                    break
                else:
                    print("密码错.")
            else:
                print("你呀输入的次数太多了.")
        else:
            print("你呀想干嘛,输入的钱不对.")
    else:
        print("输入错误.")

def print_bill(user):


    bill_sum = 1000

    return bill_sum


def cash_transfor(user1, user2):


    print("cash_transfor")
    pass

def print_card_log(user):
    """

    :param user: 登陆的用户
    :return: 返回上月账单日志表格
    """
    user_dict = file_manage.file_read(user_file)
    print("你的卡号是:%s,信用额度:%s,余额:%s" % (user_dict[user][2],user_dict[user][4],user_dict[user][5]))
    print("-"*50)
    print("时间\t用户\t操作\t费用")
    fr = open(atm_log_file, "r")
    card_log = []
    for line in fr:
        if user in line:
            #print(line.replace(",", "\t"))
            card_log.append(line)
    fr.close()

    card_log_day = 22
    pay_back_day = 10

    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day

    if month == 1:
        if day > card_log_day:
            day_start = "%s-%s-%s" % (year-1,12,card_log_day)
            day_end = "%s-%s-%s" % (year,month,card_log_day)
        else:
            day_start = "%s-%s-%s" % (year-1,11,card_log_day)
            day_end = "%s-%s-%s" % (year-1,12,card_log_day)
    if month == 2:
        if day > card_log_day:
            day_start = "%s-%s-%s" % (year,month-1,card_log_day)
            day_end = "%s-%s-%s" % (year,month,card_log_day)
        else:
            day_start = "%s-%s-%s" % (year-1,12,card_log_day)
            day_end = "%s-%s-%s" % (year,month-1,card_log_day)
    else:
        if day > card_log_day:
            day_start = "%s-%s-%s" % (year,month-1,card_log_day)
            day_end = "%s-%s-%s" % (year,month,card_log_day)
        else:
            day_start = "%s-%s-%s" % (year,month-2,card_log_day)
            day_end = "%s-%s-%s" % (year,month-1,card_log_day)



    for line in card_log:
        if day_start in line:
            index_start = card_log.index(line)
            break
        else:
            index_start = 0
    for line in card_log:
        if day_end in line:
            index_end = card_log.index(line)
            break
        else:
            index_end = -1

    for line in card_log[index_start:index_end+1]:
        print(line.replace(",", "\t"))




def cash_back(user):
    """

    :param user: 登陆的用户
    :return: 还款函数
    """
    user_dict = file_manage.file_read(user_file)
    input_num = input("输入你呀要还的钱,穷光蛋:")
    if input_num.strip().isdigit():
        if int(input_num) > 0:
            for i in range(3):
                input_pass = input("输入你呀的在支付密码:")
                if input_pass == user_dict[user][3]:
                    user_dict[user][5] += int(input_num)
                    file_manage.file_write(user_dict, user_file)
                    log.write_atm_log(user,"还款","-" + str(int(input_num)))
                    break
                else:
                    print("密码错.")
            else:
                print("你呀输入的次数太多了.")
        else:
            print("你呀想干嘛,输入的钱不对.")
    else:
        print("输入错误.")



#print(create_card("user01"))

def atm(user):
    while True:
        print('''
    1.  提现
    2.  购物
    3.  打印上月账单
    4.  转账
    5.  每月消费流水
    6.  信用卡还款
        ''')
        choose = input("输入你的选择(Q:退出)：")
        if choose.strip() == "1":
            cash_out(user)
        elif choose.strip() == "2":
            shop_with_card(user)
        elif choose.strip() == "3":
            print_bill(user)
        elif choose.strip() == "4":
            user2 = input()
            cash_transfor(user,user2)
        elif choose.strip() == "5":
            print_card_log(user)
        elif choose.strip() == "6":
            cash_back(user)
        elif choose.strip().lower() == "q":
            break
        else:
            print("输入错误。")

        if input("是否退出（Y/N？）").strip().lower() == "y":
            break


