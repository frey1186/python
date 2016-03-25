#!/usr/bin/env python3

# 登陆接口：
# 输入用户名，成功后显示欢迎信息，相同用户名输错三次后锁定该用户
#
# 版本：v1.0
# 作者：felo
# 时间：2015-12-30 21:15:37


user_password = {}  #临时存放用户名和密码
user_locked = []    #临时存放被锁定的用户名
input_user = []     #临时存放本次运行中输入的所有用户名

##读取存放用户信息的文件
file = open(r'user.txt', 'r')
for line in file.readlines():
    if not line.startswith('#'):
        #将每行中第一个和第二个字段，写入user_password字典中
        user_password[line.strip().split(':')[0]] = line.strip().split(':')[1]
        #将每行中第三个字段为1的用户写入user_locked中
        if int(line.strip().split(':')[2]) == 1:
            user_locked.append(line.strip().split(':')[0])
file.close()


##判断用户和密码正确性
flag = 1
while flag:
    user = input('请输入用户名：')
    password = input('请输入密码：')
    #如果用户在user_locked中，则显示用户已被锁定，并继续循环
    if user in user_password and user in user_locked:
        print('\n用户已经被锁定。\n')
    #如果用户名和密码正确，则显示欢迎词，并推出循环
    elif user in user_password and user_password[user] == password:
        print('\n欢迎登陆，%s\n' % user)
        break
    else:
        print('\n用户名或密码输入错误。\n')
        input_user.append(user)
        #判断用户是否已经错误登陆三次，锁定
        for i in input_user:
            if input_user.count(i) >= 3:
                print('用户%s登陆三次错误，已锁定。' % i)
                user_locked.append(i)
                flag = 0
                break


##将用户名，密码以及锁定标记重新写入用户信息文件中
file = open(r'user.txt', 'w')
#对于原有用户，修改锁定标记后重新写入
file.write('#user_name:password:is_locked:\n')
for i in user_password:
    line = i + ':' + user_password[i]
    if i in user_locked:
        line += ':1:\n'
    else:
        line += ':0:\n'
    file.write(line)
#对于不存在的用户，但被锁定，同样记录到用户信息文件中
for j in user_locked:
    if j in user_locked and j not in user_password:
        #记录格式为 '用户名::1\n'
        file.write(j + '::1:\n')
file.close()



