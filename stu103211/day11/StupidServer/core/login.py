#!/usr/bin/env python3
#_*_coding:utf-8_*_

import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
# print(sys.path)

from sqlalchemy import and_
from core import models



def user_login_sserver():
    """
    用户登陆堡垒机接口，验证用户输入是否匹配数据库表中数据，允许重试次数为3次。
    :return: 完成后返回登陆上的用户。
    """
    retry_count = 3
    while True:
        username = input("input your username:").strip()
        password = input("input your password:")
        #获取数据库数据
        res = models.session.query(models.UserProfile).filter(
                and_(models.UserProfile.username == username,
                     models.UserProfile.password == password)).all()
        if res:
            print("welcome login the stupidserver,%s"% username)
            return username
        else:
            retry_count -= 1
            if retry_count == 0:
                print("stupid boy,goodbye...")
                break
            print("wrong username or password,you can retry %s times. " % retry_count)



if __name__ == '__main__':
    user_login_sserver()