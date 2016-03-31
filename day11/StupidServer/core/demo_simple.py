
import base64
import getpass
import os
import socket
import sys
import traceback
from paramiko.py3compat import input

import paramiko


def exce_cmd(hostname, username, password,port=22):
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



    port = 22


    # now, connect and use paramiko Client to negotiate SSH2 across the connection
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy())
        print('*** Connecting...')
        if not UseGSSAPI or (not UseGSSAPI and not DoGSSAPIKeyExchange):
            client.connect(hostname, port, username, password)
        else:
            # SSPI works only with the FQDN of the target host
            hostname = socket.getfqdn(hostname)
            try:
                client.connect(hostname, port, username, gss_auth=UseGSSAPI,
                               gss_kex=DoGSSAPIKeyExchange)
            except Exception:
                #password = getpass.getpass('Password for %s@%s: ' % (username, hostname))
                client.connect(hostname, port, username, password)

        chan = client.invoke_shell()
        print(repr(client.get_transport()))
        print('*** Here we go!\n')
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

if __name__ == '__main__':
    exce_cmd("localhost","felo","felo")