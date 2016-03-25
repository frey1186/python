本项目为修改ha配置文件的简易程序，可以进行查看，增加，删除记录。

###Install
可在python3.x环境中执行，不适用于python2.x。
执行：
\#cd code_dir
\#./homework.py 或者：#python3 homework.py
开始选择即可，输入数字和回车进行选择。

###Credits：
编写人员：felo

###History：
v1.0  2016-01-19 21:00:06

###Manifest：
https://www.processon.com/diagraming/564954c4e4b0e52415ca48ba
总共包含2个函数。
- get_record(backend, config_file)
    得到配置文件的ha记录列表和整个文件列表
    :param backend: 输入backend
    :param config_file: 配置文件名称
    :return:对应backend的ha记录和整个配置文件列表

- ha_record():
    主函数
    1、获取ha记录
    2、增加ha记录
    3、删除ha记录
    4、修改ha记录
    分成4个选择来编写，分别实现获取，增加，删除和修改四个功能，
    如果输入q退出函数，输入其他输出错误。



###运行举例
D:\media\stu103211\day03>
D:\media\stu103211\day03>python3 homework.py

            1、获取ha记录
            2、增加ha记录
            3、删除ha记录
            4、修改ha记录

请输入操作序号(Q：退出)：1
请输入backend：test.oldboy.org
--------------------------------------------------------------------------------

backend: test.oldboy.org
1        server 100.1.7.9 100.1.7.9 weight 20 maxconn 30
--------------------------------------------------------------------------------


            1、获取ha记录
            2、增加ha记录
            3、删除ha记录
            4、修改ha记录

请输入操作序号(Q：退出)：2
请输入ha记录(请用“”作为字符串引号)：{"backend": "test.oldboy.org","record":{"s
erver": "100.1.7.999","weight": 20,"maxconn": 30}}
添加成功。

            1、获取ha记录
            2、增加ha记录
            3、删除ha记录
            4、修改ha记录

请输入操作序号(Q：退出)：1
请输入backend：test.oldboy.org
--------------------------------------------------------------------------------

backend: test.oldboy.org
1        server 100.1.7.9 100.1.7.9 weight 20 maxconn 30
2        server 100.1.7.999 100.1.7.999 weight 20 maxconn 30
--------------------------------------------------------------------------------


            1、获取ha记录
            2、增加ha记录
            3、删除ha记录
            4、修改ha记录

请输入操作序号(Q：退出)：3
请输入ha记录(请用“”作为字符串引号)：{"backend": "test.oldboy.org","record":{"s
erver": "100.1.7.999","weight": 20,"maxconn": 30}}
删除成功。

            1、获取ha记录
            2、增加ha记录
            3、删除ha记录
            4、修改ha记录

请输入操作序号(Q：退出)：1
请输入backend：test.oldboy.org
--------------------------------------------------------------------------------

backend: test.oldboy.org
1        server 100.1.7.9 100.1.7.9 weight 20 maxconn 30
--------------------------------------------------------------------------------


            1、获取ha记录
            2、增加ha记录
            3、删除ha记录
            4、修改ha记录

请输入操作序号(Q：退出)：q

D:\media\stu103211\day03>
