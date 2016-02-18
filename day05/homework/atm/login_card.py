import json

# card_id_dict = {
#     "user01": ["62222000000000001223", "password", 15000],
#     "user02": ["62222000000000001224", "password", 15000],
#     "user03": ["62222000000000001225", "password", 15000],
#     "user04": ["62222000000000001226", "password", 15000],
# }

card_id_file = "atm/card_id_dict.txt"


def login_card(user):
    fr = open(card_id_file, "r")
    card_id_dict = json.load(fr)
    fr.close()
    print("你呀的卡号：%s" % card_id_dict[user][0])
    for i in range(3):
        password = input("输入你呀的支付密码：")
        if card_id_dict[user][1] == password:
            print("欢迎登陆。")
            break
        else:
            print("密码错误，还有%s次机会" % (2-i))
    else:
        print("错误。")

