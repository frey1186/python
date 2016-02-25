import settings
import commodity



class Shop(object):
    def __init__(self):
        pass

    def __list_m(self, dict1, type, index=0):
        list1 = []
        for i,key in enumerate(dict1):
            list2 = dict1[key]
            list1.append((i+index,type,key,list2[0],list2[1],list2[2]))
        return list1

    def list_all(self):
        print("序号\t类型\t名称\t增加值\t价值(元)\t库存")
        index = 0
        list1 = []
        list1 += self.__list_m(settings.magic_durgs_dict,"魔法",index)
        index += len(settings.magic_durgs_dict)
        list1 += self.__list_m(settings.life_durgs_dict,"生命",index)
        index += len(settings.life_durgs_dict)
        list1 += self.__list_m(settings.weapon_dict,"武器",index)
        for line in list1:
            for i in line:
                print(i,"\t",end="")
            print("")
        return list1

    #商店的功能还未完全实现....
    def buy(self,product):
        pass


