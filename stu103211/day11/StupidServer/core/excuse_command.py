import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
#print(sys.path)

import base64
import getpass
import os
import socket
import sys
import traceback
from paramiko.py3compat import input

import paramiko
from core import handles

def excuse_command(hostname, username, password,port=22):
    """
    实现类shell的功能
    :param hostname: 被管理机的ip地址
    :param username: 用户名
    :param password: 密码
    :param port: 端口，默认22
    :return:
    """

    try:
        import interactive
    except ImportError:
        from . import interactive
    UseGSSAPI = True             # enable GSS-API / SSPI authentication
    DoGSSAPIKeyExchange = True
    # now, connect and use paramiko Client to negotiate SSH2 across the connection
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # client.set_missing_host_key_policy(paramiko.WarningPolicy())
        #print('*** Connecting...')
        # if not UseGSSAPI or (not UseGSSAPI and not DoGSSAPIKeyExchange):
        #     client.connect(hostname, port, username, password)
        # else:
        #     # SSPI works only with the FQDN of the target host
        #     hostname = socket.getfqdn(hostname)
        #     try:
        #         client.connect(hostname, port, username, gss_auth=UseGSSAPI,
        #                        gss_kex=DoGSSAPIKeyExchange)
        #     except Exception:
        #         #password = getpass.getpass('Password for %s@%s: ' % (username, hostname))
        #         client.connect(hostname, port, username, password)

        client.connect(hostname, port, username, password)


        chan = client.invoke_shell()
        #print(repr(client.get_transport()))
        #print('*** Here we go!\n')
        interactive.interactive_shell(chan)
        chan.close()
        client.close()

    except Exception as e:
        print('*** Caught exception: %s: %s' % (e.__class__, e))
        traceback.print_exc()
        try:
            client.close()
        except:
            pass
        sys.exit(1)

# if __name__ == '__main__':
#
#
#     user_list = handles.choose("felo")
#     #[host.hostname,host.ip_addr,host_user.username,host_user.password]
#     excuse_command(user_list[1],  #host.ip_addr,
#                    user_list[2],  #host_user.username
#                    user_list[3],  #host_user.password
#                    )