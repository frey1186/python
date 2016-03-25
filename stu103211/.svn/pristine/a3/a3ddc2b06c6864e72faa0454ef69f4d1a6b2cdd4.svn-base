#from user import file_manage
atm_log_file = "log/atm_log.txt"
shop_log_file = "log/shop_log.txt"
import time,datetime

def write_atm_log(user,op,bill):
    """

    :param user: 登陆的用户
    :param op: 进行的操作
    :param bill: 涉及的钱数,还款-,付款+
    :return: 返回写入日志文件
    """
    #时间,用户,操作,费用(还款-,付款+)
    write_str = "%s,%s,%s,%s" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),user,op,bill)
    fw = open(atm_log_file,"a")
    fw.write(write_str+"\n")
    fw.close()


# def read_atm_log():
#     pass
#
#
# def write_shop_log():
#     pass
#
#
# def read_shop_log():
#     pass


#
# # a = datetime.datetime.today()
# # print(a)
# a = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# #b = datetime.datetime.day
#
# # b = a.split(" ")[0].split("-")[2]
# # print(a,type(a))
# # print(b,type(b))
#
#
# card_log_day = 22
# pay_back_day = 10
#
#
#
# year = datetime.datetime.now().year
# month = datetime.datetime.now().month
# day = datetime.datetime.now().day
#
# if month == 1:
#     if day > card_log_day:
#         day_start = "%s-%s-%s" % (year-1,12,card_log_day)
#         day_end = "%s-%s-%s" % (year,month,card_log_day)
#     else:
#         day_start = "%s-%s-%s" % (year-1,11,card_log_day)
#         day_end = "%s-%s-%s" % (year-1,12,card_log_day)
# else:
#     if day > card_log_day:
#         day_start = "%s-%s-%s" % (year,month-1,card_log_day)
#         day_end = "%s-%s-%s" % (year,month,card_log_day)
#     else:
#         day_start = "%s-%s-%s" % (year,month-2,card_log_day)
#         day_end = "%s-%s-%s" % (year,month-1,card_log_day)
#
#
# day = datetime.datetime.now()
#
#
