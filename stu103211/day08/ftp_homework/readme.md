本项目ftp服务器，可以用户登陆，下载文件，上传文件，切换目录。
目前只实现了用户登陆验证和下载文件的功能。


###Install
可在windows python3.x环境中执行，不适用于python2.x。在linux中未做测试
执行：
\#cd code_dir
打开服务器
python3 ftp_server.py
开始使用客户端
python3 ftp_client.py


###Credits：
编写人员：felo

###History：
v1.0  2016-3-10 21:41:09

###Manifest：
####流程图：
http://www.processon.com/diagraming/56dbc6c9e4b097bfa12589f8

####设计思路：

ftp_server设计：
使用pickle方式将用户名和密码存入文件中，通过sockect接受用户发来的用户名和加密后
的密码；
完成用户验证后开始接受client的命令；
分析client的命令，通过反射的方式，将command_hander类中的方法进行执行，这里只实现了下载文件的部分。

ftp_client设计：
向ftp_server传送用户名和密码，得到验证后，输入操作。
操作内容同样使用反射的方式，将interact类中的方法实行，


如类中的get方法：
首先服务器发送“类型，文件名，文件长度”信息给client
client回复确认消息
server开始读文件，每次读1024，发送1024长度，更新md5值
client开始写文件，每次写1024
完成后client发送接受文件完成消息
server接受后，发送md5值
client计算一下新文件的md5值，后进行比较，一致就完成，不一致删除接受到的文件



####举例

```python

C:\Python34\python3.exe D:/media/python/ftp_homework/ftpclient/modules/interactions.py
用户名：felo
密码：password
auth secuss.
ftp>get 123.PNG
[##################################################]100.00% --> Done
ftp>put s12.png
[##################################################]100.00% --> Done
ftp>exit

```