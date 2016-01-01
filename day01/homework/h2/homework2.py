#!/usr/bin/env python3

#多级菜单
#可以选择显示下一层菜单，可以返回上一层，或直接退出
#
# 版本：v1.0
# 作者：felo
# 时间：2015-12-31 23:28:21



#定义菜单字典，最后一级使用list，其他级别都是用dict
dict1 = {
'家用电器':{
    '大家电':['平板电视','空调','冰箱','洗衣机','家庭影院DVD','迷你音响'],
    '生活电器':['电风扇','冷风扇','净化器','加湿器','扫地机器人'],
    '厨房电器':['电压力锅','电饭煲','豆浆机','面包机','咖啡机']
        },
'手机数码':{
    '手机通讯':['手机','对讲机','以旧换新'],
    '京东通信':['选号中心','自助服务'],
    '运营商':['合约机','办套餐','选号码','装宽带'],
        },
'电脑办公':{
    '电脑整机':['笔记本','超极本','游戏本','平板电脑','平板电脑配件','台式机','一体机','服务器'],
    '电脑配件':['CPU','主板','显卡''硬盘','SSD固态硬盘','内存','机箱','电源','显示器','刻录机'],
    '外设产品':['鼠标','键盘','网络仪表仪器','U盘','移动硬盘'],
        }
}


menu = dict1
layer_count = 0     #层级参数
menu_list = []      #临时保存每次迭代的menu
choose_list = []    #临时保存用户选择的内容

while True:
    #打印menu或者menu的keys
    count = 0
    for i in menu:
        print(count,'\t',i)
        count += 1
    #输入选择
    num = input('\n输入你的选择[b:Back,q:Quit]:')
    #如果是数字，则转成int，如果是中文，则记录前面的标记
    try:
        num = int(num)
    except:
        try:
            num = list(menu.keys()).index(num)
        except:
            pass
    #如果num是数字，且小于menu的长度
    if isinstance(num, int) and num in range(len(menu)):
        #如果menu是list的话，说明已经是字典的最后一层，输出最后选择
        if isinstance(menu, list):
            choose_list.append(menu[num])                 #追加choose_list
            print('\n你的选择是 %s' % choose_list[0]
                  +'->'+choose_list[1]+'->'+choose_list[2]+'\n')
            break
        #如果menu是dict，则将选择记录下来，然后将menu迭代成下一层dict或者list
        elif isinstance(menu,dict):
            menu_list.append(menu)                        #追加menu_list
            choose_list.append(list(menu.keys())[num])    #追加choose_list
            print('\n已选择：%s\n'% choose_list)                #打印已经选择的内容
            menu = list(menu.values())[num]                 #迭代下一层menu
            layer_count += 1                                #层级数+1
            continue

    elif num == 'b' or num == 'B':             #输入b，返回上一层
        if layer_count == 0:                   #如果层级参数为0，显示不能返回
            print('最高层，不能返回。请重新选择：')
        else:
            layer_count -= 1                    #层级参数-1
            menu = menu_list.pop()              #将menu_list最后一项返回给menu
            choose_list.pop()                   #删除choose_list最后一项
            print('\n已选择：%s\n'% choose_list)
        continue

    elif num == 'q' or num == 'Q':
        print('退出了，拜拜。')
        break
    else:
        print('输入错误，重新输入')
        continue
