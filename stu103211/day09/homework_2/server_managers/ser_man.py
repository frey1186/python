import paramiko
import logging
import threading
import re
import configparser
from multiprocessing import Process



logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='ser_man.log',
                filemode='a')


def cmd_tranfer(hostname, port, username, password, cmd):
    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname=hostname, port=port, username=username, password=password)

    # 执行命令
    stdin, stdout, stderr = ssh.exec_command(cmd)
    # 获取命令结果
    # out = stdout.read()
    err = stderr.read()
    #print("out:",result.decode())
    #print("err:",result2.decode())
    if not err:
        print("[%s] '%s' 执行成功" % (hostname,cmd))
        logging.info("[%s] '%s' 执行成功" % (hostname,cmd))
    else:
        logging.error(err)
        print(err.decode())
    # 关闭连接
    ssh.close()

def batch_cmd_tranfer(host_group,cmd):
    t_list = []
    for host in host_group:
        hostname = config.get(host,"hostname")
        username = config.get(host,"username")
        password = config.get(host,"password")
        #多进程
        t = Process(target=cmd_tranfer,args=(hostname,22,username,password,cmd))
        #多线程
        #t = threading.Thread(target=cmd_tranfer,args=(hostname,22,username,password,cmd))
        t.start()
        t_list.append(t)
    for i in t_list:
        i.join()


def file_tranfer(hostname,port,username,password,interact,source_file,dest_file):
    sock = (hostname,port)
    transport = paramiko.Transport(sock)
    transport.connect(username=username,password=password)

    sftp = paramiko.SFTPClient.from_transport(transport)
    if hasattr(sftp,interact):
        func = getattr(sftp,interact)
        try:
            func(source_file, dest_file)
            print("[%s]%s %s 成功。"% (hostname,interact,source_file))
            logging.info("[%s]%s %s 成功。"% (hostname,interact,source_file))
        except Exception as e:
            logging.error(e)
            print(e)

    transport.close()

def batch_file_tranfer(group_name):
    while True:
        interact = input("get or put:").strip()
        if interact.lower() == "bye":
            break
        if interact == "":
            continue
        if interact not in ["put","get"]:
            continue
        if interact.lower() == "bye":
            break
        source_file = input("sorce_file:").strip()
        if source_file =="":
            continue
        if source_file.lower() == "bye":
            break
        dest_file = input("dest_file:").strip()
        if dest_file == "":
            continue
        if dest_file.lower() == "bye":
            break

        t_list = []
        for host in group_name:
            #使用多进程序
            #t = Process(target=file_tranfer,args=(host,22,group_name[host][0],
            #             group_name[host][1],interact,source_file,dest_file))
            #多线程
            t = threading.Thread(target=file_tranfer,args=(host,22,group_name[host][0],
                         group_name[host][1],interact,source_file,dest_file))
            t.start()
            t_list.append(t)
        for i in t_list:
            i.join()

            #顺序执行
            #file_tranfer(host,22,group_name[host][0],
            #            group_name[host][1],interact,source_file,dest_file)


def re_host_group(host_group, re_str):
    """
    正则表达式处理传入的主机列表
    :param host_group: 主机列表
    :param re_str: 正则表达式
    :return: 返回处理后的主机列表，如果沒有就返回空列表
    """
    host_list = []
    for host in host_group:
        if re.search(re_str, host):
            host_list.append(host)
    return host_list

def cmd_line_handle(cmd_line):
    """
    将命令分成四段
    :param cmd_line: 输入的命令
    :return: 返回列表【salt，正则表达式，命令类型，命令内容】
    """
    g = re.search('(salt) "(.*)" (.*) "(.*)"', cmd_line)
    return g.groups()

def print_help():
    print("""
    please input right command.
    ex:
        >>salt "*" cmd.run "ls -al /" :excuse the "ls -al / " on all hosts.
        >>exit : for exit
    """)

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("sm.conf")
    all_host = config.sections()

    while True:
        input_cmd = input(">>").strip()
        if len(input_cmd) == 0 :continue
        if input_cmd == "exit":break
        try:
            cmd_list = cmd_line_handle(input_cmd)
        except:
            cmd_list = []
        if cmd_list[0] != "salt":
            print_help()
            continue
        try:
            host_be_opeated = re_host_group(all_host,cmd_list[1])
            if cmd_list[2] == "cmd.run":
                batch_cmd_tranfer(host_be_opeated,cmd_list[3])
        except IndexError as e:
            print(e)





