#!/usr/bin/env python3
#_*_coding:utf-8_*_

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
#print(sys.path)

from core import models

def choose_group(user):
    """
    通过在查询Userprofile和Group表，查找到用户所有权限的组，打印出来，进行选择
    :param user: Userprofile表中的用户，就是堡垒机用户
    :return: 返回选择的组名称或组ID
    """
    #查询UserProfile中groups
    res = models.session.query(models.UserProfile).filter(models.UserProfile.username==user).first()
    group_id_list = []
    group_name_list = []
    if res.groups:
        for group in res.groups:
            print("#"*50,"\n","GroupID:",group.id,"\tGroupName:",group.name)
            group_id_list.append(group.id)
            group_name_list.append(group.name)
        for i in range(3):
            choose = input("[group id]:").strip()
            if choose.isdigit():
                if int(choose) in group_id_list:
                    id = group_id_list.index(int(choose))
                    #print('Chosen GroupName:',group_name_list[id])
                    return group_name_list[id]
                else:
                    print("again...")
            else:
                print("again...")
    else:
        print("wrong......")
    

def choose_host(user,group):
    """
    选择堡垒机用户和组中的要执行命令的主机名和用户名
    :param user: 堡垒机用户名
    :param group: 所在组
    :return:返回选中的主机，用户名，IP地址，密码
    """
    #UserProfile表中查出主机用户
    user_item = models.session.query(models.UserProfile).filter(models.UserProfile.username==user).first()
    #Group表中查出主机用户，两者取交集，就是需要的主机用户列表。
    group_item = models.session.query(models.Group).filter(models.Group.name==group).first()
    #将两个列表转换为set，取交集，重新转为list
    host_user_list = list(set(user_item.host_list) & set(group_item.host_list))
    #print("host_user_list:",host_user_list)
    #开始选择：
    host_dict = {}
    if host_user_list:
        for host_user in host_user_list:
            #从host表中将与host_user对应的host相关信息取出
            host = models.session.query(models.Host).\
                filter(models.Host.id==host_user.host_id).first()
            #print("host",host)
            print(host_user.id,"\tHostname:",host.hostname,host.ip_addr,host_user.username)

            #放入一个字典中
            host_dict[host_user.id] = \
                [host.hostname,host.ip_addr,host_user.username,host_user.password]

        #最多三次选择
        for i in range(3):
            choose = input("[host id]:").strip()
            if choose.isdigit():
                if int(choose) in host_dict:
                    #print('Chosen Hostname and User:%s.%s' % (host_dict[int(choose)][0],
                    #      host_dict[int(choose)][2]))
                    return host_dict[int(choose)]
                else:
                    print("again...")
            else:
                print("again...")
    else:
        print("wrong......")


def choose(localuser):
    """
    集成上面两个函数
    :param localuser:
    :return:
    """
    group = choose_group(localuser)
    host_user_list = choose_host(localuser,group)
    return host_user_list
    #[host.hostname,host.ip_addr,host_user.username,host_user.password]



if __name__ == '__main__':

    choose("felo")
    
    