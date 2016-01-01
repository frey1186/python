本项目为登陆接口，验证用户登陆信息，在输入错误超过三次会将该用户锁定

###Install
可在python3.x环境中执行，不适用于python2.x。
执行：
\#cd code_dir
\#./homework1.py 或者：#python3 homework.py
根据提示输入用户名和密码即可。


###Credits：
编写人员：杨飞龙

###NEWS：
无

###History：
v1.0  2015-12-30 21:31:23

###Copying：
GNU.

###License：

###Manifest：
包含两个文件：
- user.txt：记录系统现有用户的信息，每个用户占一行，每行格式为 “用户名：密码：1或0：”，用于分别记录用户名，密码，和锁定标记，其中1为锁定，0为未锁定
- homework.py:主程序，分成三个部分，第一部分读取user.txt文件，第二部分判断登陆情况，第三部分将新的内容重新写入user.txt文件

FAQ：
无

TAGS：
无