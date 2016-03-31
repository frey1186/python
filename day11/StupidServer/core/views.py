#!/usr/bin/env python3
#_*_coding:utf-8_*_
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


