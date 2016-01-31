__author__ = 'felo'

import sys
import os
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_dir)



from config import setting

def auth(configs):
    if configs.DATABASE["user"] == "root" and configs.DATABASE["password"] == "123123":
        print("welcom login database")
        return True
    else:
        print("error....")


def select(name, age):
    res = auth(setting)

    if res:
        return name,age
