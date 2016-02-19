from user import file_manage
user_file = "user/user.txt"
atm_log_file = "log/atm_log.txt"

def change_edu():
    user_dict = file_manage.file_read(user_file)
    for i in range(3):
        user = input("输入您老人家要修改的用户:")
        if user in user_dict:
            input_num = input("输入额度:")
            if input_num.strip().isdigit():
                user_dict[user][4] = int(input_num)
                file_manage.file_write(user_dict, user_file)
                print("修改额度成功,用户:%s,额度:%s" % (user, user_dict[user][4]))
                break
            else:
                print("输入错误")
        else:
            print("用户错误.")
    else:
        print("输入次数太多了")


def watch_atm_log():
    fr = open(atm_log_file,"r")
    print("时间\t用户\t操作\t费用")
    if fr:
        for line in fr:
            print(line.replace(",", "\t"))
    fr.close()

def atm_manage():
    while True:
        print('''
    1.  修改信用卡额度
    2.  查看操作日志
        ''')
        choose = input("输入你的选择(Q:退出)：")

        if choose.strip() == "1":
            change_edu()
        elif choose.strip() == "2":
            watch_atm_log()
        elif choose.strip().lower() == "q":
            break
        else:
            print("输入错误。")

        if input("是否退出（Y/N？）").strip().lower() == "y":
            break



