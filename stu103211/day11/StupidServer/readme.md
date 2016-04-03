本项目为stupidserver，堡垒机项目
### 功能需求：

1. 【没实现】所有的用户操作日志要保留在数据库中
2. 【实现】每个用户登录堡垒机后，只需要选择具体要访问的设置，就连接上了，不需要再输入目标机器的访问密码
3. 【实现】允许用户对不同的目标设备有不同的访问权限，例:
    - 对10.0.2.34 有mysql 用户的权限
    - 对192.168.3.22 有root用户的权限
    - 对172.33.24.55 没任何权限
4. 【实现】分组管理，即可以对设置进行分组，允许用户访问某组机器，但对组里的不同机器依然有不同的访问权限
5. 【没实现】stupidserver管理员视角，批量导入数据库信息

###Install
可在python3.x环境中ubuntu下执行，不适用于python2.x。
执行：

`# cd code_dir`
`# python3 stupidserver.py`
开始选择即可，输入数字和回车进行选择。

###Credits：
编写人员：felo

###History：
v1.0  2016-4-1 10:40:36

### Manifest：
blog：
http://www.cnblogs.com/felo/
表结构：
https://www.processon.com/diagraming/56fbcc9de4b0d2c1b15ec116
```shell
D:\media\github\python\day11\StupidServer>tree /F
卷 data 的文件夹 PATH 列表
卷序列号为 8C3B-5521
D:.
│  readme.md
│  __init__.py
│
├─bin
│      stupidserver.py
│      __init__.py
│
├─conf
│      regedit.py
│      settings.py
│      ss.yml
│      __init__.py
│
├─core
│      actions.py
│      excuse_command.py
│      handles.py
│      interactive.py
│      login.py
│      models.py
│      views.py
│      __init__.py
│
└─log
        __init__.py

```

###运行举例
```python

felo@felo-virtual-machine:~/github/day11/StupidServer/bin$ python3 stupidserver.py
Help message:pleas input the args...
like:stupidserver.py cmd

---> initialize
---> insertdata
---> cmd
---> syncdb
felo@felo-virtual-machine:~/github/day11/StupidServer/bin$ python3 stupidserver.py syncdb
the database is syncing....
the database is synced.
felo@felo-virtual-machine:~/github/day11/StupidServer/bin$ python3 stupidserver.py insertdata
felo@felo-virtual-machine:~/github/day11/StupidServer/bin$ python3 stupidserver.py initialize
felo@felo-virtual-machine:~/github/day11/StupidServer/bin$ python3 stupidserver.py cmd
input your username:felo
input your password:felo
welcome login the stupidserver,felo
##################################################
 GroupID: 1 	GroupName: g1
[group id]:1
1 	Hostname: localhost 127.0.0.1 felo
[host id]:1
Welcome to Ubuntu Xenial Xerus (development branch) (GNU/Linux 4.4.0-6-generic x86_64)

 * Documentation:  https://help.ubuntu.com/
Last login: Fri Apr  1 10:34:32 2016 from 127.0.0.1
felo@felo-virtual-machine:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:83:63:25 brd ff:ff:ff:ff:ff:ff
    inet 192.168.19.110/24 brd 192.168.19.255 scope global dynamic ens33
       valid_lft 1803sec preferred_lft 1803sec
    inet6 fe80::20c:29ff:fe83:6325/64 scope link
       valid_lft forever preferred_lft forever
felo@felo-virtual-machine:~$ exit
注销

*** EOF
##################################################
 GroupID: 1 	GroupName: g1
[group id]:2
again...
[group id]:3
again...
[group id]:1
1 	Hostname: localhost 127.0.0.1 felo
[host id]:2
again...
[host id]:1
Welcome to Ubuntu Xenial Xerus (development branch) (GNU/Linux 4.4.0-6-generic x86_64)

 * Documentation:  https://help.ubuntu.com/
Last login: Fri Apr  1 10:44:19 2016 from 127.0.0.1
felo@felo-virtual-machine:~$ exit
注销

*** EOF
##################################################
 GroupID: 1 	GroupName: g1
[group id]:


```
