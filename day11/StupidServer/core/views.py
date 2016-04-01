#!/usr/bin/env python3
#_*_coding:utf-8_*_

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
#print(sys.path)

from core import login
from core import handles
from core import excuse_command
from core import models


def syncdb():
    print("the database is syncing....")
    models.Base.metadata.create_all(models.engine) #创建所有表结构
    print("the database is synced.")


def insert_data():
    pass




def initialize():
    pass




def log_write():
    #models.session.
    pass


def cmd():
    localuser = login.user_login_sserver()
    while True:
        user_list = handles.choose(localuser)
        #[host.hostname,host.ip_addr,host_user.username,host_user.password]
        excuse_command.excuse_command(user_list[1],  #host.ip_addr,
                   user_list[2],  #host_user.username
                   user_list[3],  #host_user.password
                   )










