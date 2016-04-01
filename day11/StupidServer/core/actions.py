#!/usr/bin/env python3
#_*_coding:utf-8_*_
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
#print(sys.path)

from core import login
from core import handles
from core import excuse_command
from conf import regedit


def help_msg(actions):
    print("Help message:pleas input the args...\n"
          "like:stupidserver.py cmd\n")
    for i in actions.keys():
        print("--->",i)


def start_session():
    if len(sys.argv) <2:
        help_msg(regedit.actions)
    else:
        func = regedit.actions[sys.argv[1]]
        func()







