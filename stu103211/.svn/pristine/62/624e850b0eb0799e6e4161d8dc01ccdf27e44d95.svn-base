__author__ = 'felo'

from user import login, user_manage
from shopping import shopping, shop_list
from atm import atm, atm_manage


user = login.login()

if user:
    while True:
        if user == "admin":
            print(
                """
                1.购物商城用户管理
                2.信用卡管理
                """
            )
        else:
            print(
                """
                1.老夫要购物
                2.信用卡管理
                3.修改登陆密码
                """
            )

        input_str = input("输入您老人家的选择：(Q:退出)")
        if input_str.strip().lower() == "q":
            print("退出了。")
            break
        elif input_str.isdigit():
            if int(input_str) == 1:
                if user == "admin":
                    user_manage.user_manage()
                else:
                    shopping.shopping(user)
                    shop_list.shop_list(user)
            elif int(input_str) == 2:
                if user == "admin":
                    atm_manage.atm_manage()
                else:
                    atm.atm(user)
            elif int(input_str) == 3 and user != "admin":
                user_manage.user_change_password(user)

            else:
                print("input wrong strings or numbers. again.")
        else:
            print("input wrong strings or numbers. again.")



