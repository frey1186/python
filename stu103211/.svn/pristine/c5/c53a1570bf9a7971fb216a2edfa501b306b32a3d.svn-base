本项目批量管理服务器命令和文件传输
命令类似saltstack
>>salt "*" cmd.run "ls -al /" :excuse the "ls -al / " on all hosts.
>>exit : for exit

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
>>salt "centos01" cmd.run "df -h > /tmp/$USER.log"
salt "centos01" cmd.run "df -h > /tmp/$USER.log"
[192.168.19.104] 'df -h > /tmp/$USER.log' 执行成功
>>salt "centos01" cmd.run "df -h > /tmp/$USER.log"
salt "centos01" cmd.run "df -h > /tmp/$USER.log"
[192.168.19.104] 'df -h > /tmp/$USER.log' 执行成功
>>salt "centos" cmd.run "df -h > /tmp/$USER.log"
salt "centos" cmd.run "df -h > /tmp/$USER.log"
[192.168.19.104] 'df -h > /tmp/$USER.log' 执行成功
[192.168.19.104] 'df -h > /tmp/$USER.log' 执行成功