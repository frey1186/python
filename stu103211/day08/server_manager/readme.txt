本项目批量管理服务器命令和文件传输


###Install
LINUX中使用，开发使用centos7
执行：
\#cd code_dir
打开服务器
python3 serman.py



###Credits：
编写人员：felo

###History：
v1.0  2016-3-11 01:07:27

###Manifest：
####流程图：
http://www.processon.com/diagraming/56e1a7e4e4b026eb4ad3807c

####设计思路：

通过使用paramiko模块实现对服务器的访问和执行命令。


执行例子：
[root@centos01 serman]# python3 ser_man.py 

    1.批量执行命令
    2.分发文件
        
请输入选择：1
GROUP NAME:GROUP1
>ls -l /
[192.168.19.105] 'ls -l /' 执行成功
[192.168.19.104] 'ls -l /' 执行成功
>bye

    1.批量执行命令
    2.分发文件
        
请输入选择：q
bye
[root@centos01 serman]# python3 ser_man.py 

    1.批量执行命令
    2.分发文件
        
请输入选择：2
GROUP NAME:gro
wrong group name,again,

    1.批量执行命令
    2.分发文件
        
请输入选择：2
GROUP NAME:group
wrong group name,again,

    1.批量执行命令
    2.分发文件
        
请输入选择：2
GROUP NAME:GROUP2
get or put:GET 
get or put:get /^H
get or put:get 
sorce_file:/tmp/1.f
dest_file:/tmp 
[Errno 21] Is a directory: '/tmp'
get or put:get 
sorce_file:/tmp/1.f
dest_file:/tmp/12.f
[192.168.19.104]get /tmp/1.f 成功。
get or put:bye

    1.批量执行命令
    2.分发文件
        
请输入选择：q
bye
[root@centos01 serman]# 
