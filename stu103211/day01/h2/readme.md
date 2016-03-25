本项目为多级菜单，可以使用数字或中文选择，b返回上一级，q退出

###Install
可在python3.x环境中执行，不适用于python2.x。
执行：
\#cd code_dir
\#./homework2.py 或者：#python3 homework2.py
根据提示输入数字或中文。


###Credits：
编写人员：felo

###NEWS：
无

###History：
v1.0  2016-01-01 00:13:28

###Copying：
GNU.

###License：

###Manifest：
包含1个文件：
- homework2.py:主程序

```flow
st=>start: 开始
e=>end: 结束
def=>operation: 定义菜单字典menu和参数

op1=>operation: 打印本级menu.keys
in=>inputoutput: 输入选择num
op2=>operation: 处理输入num
c1=>condition: num是数字且
小于列表长度
c2=>condition: menu
是列表
c3=>condition: menu
是字典
c4=>condition: num
是b或B
c5=>condition: num
是q或Q
op3=>inputoutput: 追加选择列表,
显示选择
op4=>operation: 迭代到下一层menu
（字典或列表）
op5=>operation: 返回上一层字典，
返回menu_list最后一项
op6=>inputoutput: 输出
错误

st->def->op1->in->op2->c1
c1(yes)->c2
c1(no)->c4
c2(yes)->op3->e
c2(no)->c3
c3(yes)->op4(right)->op1
c3(no)->c4
c4(yes)->op5(right)->op1
c4(no)->c5
c5(yes)->e
c5(no)->op6(right)->op1




```
