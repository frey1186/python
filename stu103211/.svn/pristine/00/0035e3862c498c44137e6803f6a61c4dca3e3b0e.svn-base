本项目为登陆接口，验证用户登陆信息，在输入错误超过三次会将该用户锁定

###Install
可在python3.x环境中执行，不适用于python2.x。
执行：
\#cd code_dir
\#./homework1.py 或者：#python3 homework.py
根据提示输入用户名和密码即可。


###Credits：
编写人员：felo

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

```flow
st=>start: 开始
e=>end: 结束
op1=>operation: 读取用户和密码及锁定文件标记的文件
op2=>operation: 将用户名和密码存放到字典中

op3=>operation: 将锁定的用户名存放到列表中

op4=>inputoutput: 输入用户名和密码
op5=>operation: 记录输入用户名到列表中

op6=>inputoutput: 输出欢迎登陆字样
op7=>inputoutput: 输出用户或密码错误
op8=>inputoutput: 输出用户（包括未注册）已经被锁定
op9=>operation: 将用户写入锁定用户列表中
op10=>operation: 将用户密码锁定用户写入文件
c1=>condition: 用户名
是否存在?
c2=>condition: 用户名
是否被锁定?
c3=>condition: 用户名密码
是否匹配?
c4=>condition: 错误次数=3?

st->op1->op2->op3->op4->c1
c1(yes)->c2
c1(no)->op7
c2(yes)->op8->op4
c2(no)->c3
c3(yes)->op6->e
c3(no)->op7->op5->c4
c4(yes)->op9->op10(left)->e
c4(no)->op4
```