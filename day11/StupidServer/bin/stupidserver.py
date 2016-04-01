#!/usr/bin/env python3
#_*_coding:utf-8_*_
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
#print(sys.path)


def main():
    from core import actions
    actions.start_session()


if __name__ == '__main__':
    main()
