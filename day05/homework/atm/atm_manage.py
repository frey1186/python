import json
import random
from atm.login_card import card_id_file
from user.login import user_file

# card_id_dict = {
#     "user01": ["62222000000000001223", "password", 15000],
#     "user02": ["62222000000000001224", "password", 15000],
#     "user03": ["62222000000000001225", "password", 15000],
#     "user04": ["62222000000000001226", "password", 15000],
# }
# fw = open("card_id_dict.txt","w")
#
# json.dump(card_id_dict, fw)
#
# fw.close()

f = open(user_file, "r")
user_dict = json.load(f)
f.close()

def create_card(user):
    fr = open(card_id_file, "r")
    card_id_dict = json.load(fr)
    fr.close()
    card_id_list = []
    for i in card_id_dict.vaules():
        card_id_list.append(i[1])
    edu = 15000
    while True:
        if user not in card_id_dict and user in user_dict and user_dict[user][1] == "unlock":
            a = str(random.randint(1, 9999))
            card_id = "622220000000000%s%s" % ("0"*(5-len(a)), a)
            if card_id not in card_id_list:
                password = input("输入密码：")
                password_again = input("再次输入密码：")
                if password == password_again:
                    card_id_dict[user] = [card_id, password, edu]
                    fw = open(card_id_file, "w")
                    json.dump(card_id_dict, fw)
                    fw.close()
                    break
                else:
                    print("两次不一致。")
        else:
            if user == "admin":
                print("wrong user name.")
            else:
                print("你呀没权限。")



def del_card():




    print("del_card")
    pass




def change_edu():
    print("change_edu")
    pass


def watch_atm_log():
    print("watch_atm_Log")
    pass





def atm_manage():
    while True:
        print('''
    1.  新建信用卡
    2.  删除信用卡
    3.  修改信用卡额度
    4.  查看操作日志
        ''')
        choose = input("输入你的选择(Q:退出)：")
        if choose.strip() == "1":
            user = input("输入用户名：")
            create_card(user)
        elif choose.strip() == "2":
            del_card()
        elif choose.strip() == "3":
            change_edu()
        elif choose.strip() == "4":
            watch_atm_log()
        elif choose.strip().lower() == "q":
            break
        else:
            print("输入错误。")

        if input("是否退出（Y/N？）").strip().lower() == "y":
            break



