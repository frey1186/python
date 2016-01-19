__author__ = 'felo'

import json

config_file = 'ha.txt'



def get_record(backend, config_file):
    '''
    得到配置文件的ha记录列表和整个文件列表
    :param backend: 输入backend
    :param config_file: 配置文件名称
    :return:对应backend的ha记录和整个配置文件列表
    '''
    record_list = []
    ha_file = open(config_file, 'r')   #打开文件
    ha_file_list = ha_file.readlines()    #读取文件
    ha_file.close()
    last_record_index = -1
    for line in ha_file_list:    #循环列表
        if backend in line:    #获取backend所在行的后几行ha记录
            next_index = ha_file_list.index(line)+1
            for i in range(next_index, len(ha_file_list)):
                if 'server' in ha_file_list[i]:
                    record_list.append(ha_file_list[i])
                    last_record_index = i
                    continue
                elif ha_file_list[i].strip() == '':
                    continue
                else:
                    break
    return record_list, ha_file_list, last_record_index



while True:
    print('''
        1、获取ha记录
        2、增加ha记录
        3、删除ha记录
        4、修改ha记录
    ''')
    num = input('请输入操作序号(Q：退出)：')

    if num.strip() == '1':    #查看ha记录
        read_backend = input('请输入backend：') #如输入：test.oldboy.org
        #读取配置文件中的record
        record_list = get_record(read_backend, config_file)[0]
        #按照格式打印出来
        print('-'*80)
        print('backend:', read_backend)
        if record_list == []:
            print('不存在记录。')
        else:
            for i in record_list:
                print(record_list.index(i)+1, '\t', i.strip())
        print('-'*80)

    elif num.strip() == '2':   #增加ha记录
        try:
            add_record_dict = json.loads(input('请输入ha记录(请用“”作为字符串引号)：'))
        except:
            print('输入错误')
            continue
        #add_record_dict = {"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}
        #合成record记录字符串
        record_str = '        server %s %s weight %d maxconn %d\n' \
                     % (add_record_dict['record']['server'], add_record_dict['record']['server'],
                        add_record_dict['record']['weight'], add_record_dict['record']['maxconn'])
        #获取config_file中的记录
        record_list = get_record(add_record_dict['backend'], config_file)
        #判断新增record是否在config_file中
        if record_str in record_list[0]:
            print('你想加入的ha记录已经在配置文件中了，不需要重复添加。')
        else:
            #如果backend在配置文件中有了：
            if 'backend %s\n' % add_record_dict['backend'] in record_list[1] and record_list[0] != []:
                #将record记录添加到文件列表中
                record_list[1].insert(record_list[2]+1, record_str)
            #如果backend在配置文件中没有：
            else:
                record_list[1].append('backend %s\n' % add_record_dict['backend'])
                record_list[1].append(record_str)

            #将新的文件列表重写回配置文件
            ha_file = open('ha.txt', 'w')
            for i in record_list[1]:
                ha_file.write(i)
            ha_file.close()
            print('添加成功。')
    elif num.strip() == '3':  #删除ha记录
        try:
            del_record_dict = json.loads(input('请输入ha记录(请用“”作为字符串引号)：'))
        except:
            print('输入错误。')
            continue
        #合成record记录字符串
        record_str = '        server %s %s weight %d maxconn %d\n' \
                     % (del_record_dict['record']['server'], del_record_dict['record']['server'],
                        del_record_dict['record']['weight'], del_record_dict['record']['maxconn'])
        #获取config_file中的记录
        record_list = get_record(del_record_dict['backend'], config_file)
        #判断新增record是否在config_file中
        if record_str in record_list[0] \
                and 'backend %s\n' % del_record_dict['backend'] in record_list[1]:
            record_list[0].remove(record_str)
            record_list[1].remove(record_str)
            if record_list[0] is []:
                record_list[1].remove('backend %s\n' % del_record_dict['backend'])
            #将新的文件列表重写回配置文件
            with open('ha.txt', 'w') as ha_file:
                for i in record_list[1]:
                    ha_file.write(i)
                ha_file.flush()
                print('删除成功。')
        else:
            print('你想删除的ha记录不在配置文件中了，无法删除。')
    elif num.strip() == '4':    #修改ha记录
        print('这个功能还没写')

    elif num.strip().casefold() == 'q':
        break
    else:
        print('输入错误。')