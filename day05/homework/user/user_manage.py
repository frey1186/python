from user import file_manage
from user.login import user_file

#
# user_dict = {
#     "user01":["password","unlock","62222000000000001221", "password", 15000, 15000, "unlock"],
#     "user02":["password","unlock","62222000000000001222", "password", 15000, 15000, "unlock"],
#     "user03":["password","unlock","62222000000000001223", "password", 15000, 15000, "unlock"],
#     "user04":["password","unlock","62222000000000001224", "password", 15000, 15000, "unlock"],
#
# }
#
# f = open("user.txt", "w")
# json.dump(user_dict,f)
# f.close()


# f = open(user_file, "r")
# user_dict = json.load(f)
# f.close()
user_dict = file_manage.file_read(user_file)

def user_list():  #列举用户
    for user in user_dict:
        if user_dict[user][1] == "locked":
            print("%s\t锁定" % user)
        elif user_dict[user][1] == "unlock":
            print("%s\t未锁定" % user)

def user_add():  #增加用户
    for i in range(3):
        user = input("input the user name:")
        if user not in user_dict:

            password = input("input your password:")
            password_conferm = input("input your password again:")
            if password == password_conferm:
                user_dict[user] = [password, "unlock"]
            else:
                print("两次输入密码不一致。")
                continue
            # f = open(user_file, "w")
            # json.dump(user_dict, f)
            # f.close()
            file_manage.file_write(user_dict, user_file)
            print("用户增加成功。")
            break
        else:
            print("用户已经存在。")
    else:
        print("你呀输入错误次数太多了。")

def user_del(user):  #删除用户
    if user in user_dict:
        conform = input("是否确定删除%s(Y or N)" % user)
        if conform.strip().lower() == "y":
            user_dict.pop("user")
            print("用户%s已删除。" % user)
            # f = open(user_file, "w")
            # json.dump(user_dict, f)
            # f.close()
            file_manage.file_write(user_dict, user_file)
            print("用户删除成功。")
        elif conform.strip().lower() == "n":
            print("返回。")
        else:
            print("输入错误。")

    else:
        print("用户%s不存在。" % user)

def user_change_password(user):  #修改用户密码
    if user in user_dict:
        for i in range(3):
            new_pass = input("输入你的新密码：")
            new_pass_conform = input("再次输入你的新密码：")
            if new_pass == new_pass_conform:
                user_dict[user][0] = new_pass
                # f = open(user_file, "w")
                # json.dump(user_dict, f)
                # f.close()
                file_manage.file_write(user_dict, user_file)
                print("用户密码修改成功。")
                break
    else:
        print("用户%s不存在。" % user)

def user_locked(user):
    if user in user_dict:
        if user_dict[user][1] == "locked":
            print("用户%s已经被锁定，不用再次锁定。" % user)
        else:
            user_dict[user][1] = "locked"
            # f = open(user_file, "w")
            # json.dump(user_dict, f)
            # f.close()
            file_manage.file_write(user_dict, user_file)
            print("用户%s锁定成功。" % user)
    else:
        print("用户%s不存在。" % user)

def user_unlock(user):
    if user in user_dict:
        if user_dict[user][1] == "unlock":
            print("用户%s已经被解锁，不用再次解锁。" % user)
        else:
            user_dict[user][1] = "unlock"
            # f = open(user_file, "w")
            # json.dump(user_dict, f)
            # f.close()
            file_manage.file_write(user_dict, user_file)
            print("用户%s解锁成功。" % user)
    else:
        print("用户%s不存在。" % user)


def user_manage():
    while True:
        print('''
    1.  列出用户
    2.  增加用户
    3.  删除用户
    4.  修改密码
    5.  锁定用户
    6.  解锁用户
        ''')
        choose = input("输入你的选择(Q:退出)：")
        if choose.strip() == "1":
            user_list()
        elif choose.strip() == "2":
            user_add()
        elif choose.strip() == "3":
            user = input("输入要删除的用户名：")
            user_del(user)
        elif choose.strip() == "4":
            user = input("输入要修改密码的用户名：")
            user_change_password(user)
        elif choose.strip() == "5":
            user = input("输入要锁定的用户名：")
            user_locked(user)
        elif choose.strip() == "6":
            user = input("输入要解锁的用户名：")
            user_unlock(user)
        elif choose.strip().lower() == "q":
            break
        else:
            print("输入错误。")

        if input("是否退出（Y/N？）").strip().lower() == "y":
            break


# if __name__ == '__main__':
#     user_manage()

