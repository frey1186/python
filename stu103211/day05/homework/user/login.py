from user import file_manage
user_file = "user/user.txt"

def login():
    """
    登陆函数
    :return:
    """
    user_dict = file_manage.file_read(user_file)

    input_username = []
    ##判断用户和密码正确性
    while True:
        user = input('请输入用户名：')
        password = input('请输入密码：')
        #如果用户在user_locked中，则显示用户已被锁定，并继续循环
        if user in user_dict and user_dict[user][1] == "locked":
            print('\n用户已经被锁定。\n')
            return False
        #如果用户名和密码正确，则显示欢迎词，并推出循环
        elif user in user_dict and user_dict[user][0] == password:
            print('\n欢迎登陆，%s\n' % user)
            return user
        else:
            print('\n用户名或密码输入错误。\n')
            input_username.append(user)
            #判断用户是否已经错误登陆三次，锁定
            if input_username.count(user) >= 3:
                print('用户%s登陆三次错误，已锁定。' % user)
                if user_dict.get(user):
                    user_dict[user][1] = "locked"
                else:
                    user_dict[user] = ["", "locked"]
                file_manage.file_write(user_dict, user_file)
                return False

#
# if __name__ == '__main__':
#     login()

