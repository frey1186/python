本项目为简易购物商城，主要功能就是选择已有的商品，通过项目实现统计购物列表和余额情况。购物过程中如果
余额不足可以通过修改购物列表或者重新购物来修改。
最终输出采购列表。

###Install
可在python3.x环境中执行，不适用于python2.x。
执行：
\#cd code_dir
\#./h1.py 或者：#python3 h1.py
开始选择即可，输入数字和回车进行选择。

###Credits：
编写人员：felo

###History：
v1.0  2016-01-14 20:34:36

###Manifest：
总共包含五个函数。

- print_welcome_info()
    显示输出欢迎信息

- choose_product_list(my_money, product_dict, shopping_dict)
    选择产品，将每次选择的产品添加到shopping_dict中临时保存起来

- print_shopping_list(my_money, product_dict, shopping_dict)
    打印已经选择加入购物车的产品列表

- choose_shopping_list(my_money, product_dict, shopping_dict)
    对购物车中的产品就行修改，返回shopping_dict

- shopping()
    主函数，调用上面几个函数
