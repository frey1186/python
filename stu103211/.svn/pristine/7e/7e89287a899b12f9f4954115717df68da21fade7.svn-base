import paramiko
import logging
import threading
from multiprocessing import  Process
import settings


logging.basicConfig(level=logging.DEBUG,
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

def batch_cmd_tranfer(group_name):
    while True:
        input_cmd = input(">").strip()
        if len(input_cmd) ==0:
            continue
        if input_cmd.lower() == "bye":
            break

        t_list = []
        for host in group_name:
            #多进程
            #t = Process(target=cmd_tranfer,args=(host,22,group_name[host][0],group_name[host][1],input_cmd))
            #多线程
            t = threading.Thread(target=cmd_tranfer,args=(host,22,group_name[host][0],group_name[host][1],input_cmd))
            t.start()
            t_list.append(t)
        for i in t_list:
            i.join()

            #顺序执行
            #cmd_tranfer(host,22,group_name[host][0],group_name[host][1],input_cmd)


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

if __name__ == '__main__':
    #print(dir(settings))
    while True:
        print(
        """
    1.批量执行命令
    2.分发文件
        """
        )
        input_num = input("请输入选择：").strip()
        if input_num.lower() == "q":
            print("bye")
            break
        elif input_num not in ["1","2"]:
            continue
        groups = input("GROUP NAME:")
        if hasattr(settings,groups):
            groups_dict = getattr(settings,groups)
            if input_num == "1":
                batch_cmd_tranfer(groups_dict)
            elif input_num == "2":
                batch_file_tranfer(groups_dict)
        else:
            print("wrong group name,again,")

