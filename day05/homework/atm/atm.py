import json
card_id_dict = {
    "user01": ["62222000000000001223", "password", 15000, 15000],
    "user02": ["62222000000000001224", "password", 15000, 15000],
    "user03": ["62222000000000001225", "password", 15000, 15000],
    "user04": ["62222000000000001226", "password", 15000, 15000],
}
fw = open("card_id_dict.txt","w")

json.dump(card_id_dict, fw)

fw.close()


'''







def shop_with_card():
    print("shop_with_card")
    pass



def cash_out():
    print("cash_out")
    pass

def print_last_list():
    print("print_last_list")
    pass


def cash_transfor():
    print("cash_transfor")
    pass

def print_card_log():
    print("print_card_log")
    pass

def cash_back():
    print("cash_back")
    pass



#print(create_card("user01"))

def atm():
    while True:
        print('''
    1.  购物
    2.  提现
    3.  打印上月账单
    4.  转账
    5.  每月消费流水
    6.  信用卡还款
        ''')
        choose = input("输入你的选择(Q:退出)：")
        if choose.strip() == "1":
            cash_out()
        elif choose.strip() == "2":
            shop_with_card()
        elif choose.strip() == "3":
            print_last_list()
        elif choose.strip() == "4":
            cash_transfor()
        elif choose.strip() == "5":
            print_card_log()
        elif choose.strip() == "6":
            cash_back()
        elif choose.strip().lower() == "q":
            break
        else:
            print("输入错误。")

        if input("是否退出（Y/N？）").strip().lower() == "y":
            break


'''