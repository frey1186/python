class Commodity(object):
    """
    商品类,包含商品的所有属性,以及卖出和半价收购等方法
    """
    def __init__(self,name, type, vaule, price,num_in_stock):
        self.name = name  #名称
        self.type = type  #类型:魔法还是生命药水,还是武器
        self.vaule = vaule    #增加多少
        self.price = price    #多少钱
        self.num_in_stock = num_in_stock  #库存

    def sell(self,num_sell):  #卖出
        self.num_in_stock -= num_sell
        return self.price*num_sell

    def purchase(self,num_pur):  #半价收购
        self.num_in_stock += num_pur
        return self.price/2*num_pur


#魔法药品:
magic_durgs_dict = {
    #名称:[增加值,多少钱,库存]
    "小魔瓶":[10, 100, 10],
    "中魔瓶":[50, 150, 10],
    "大魔瓶":[100, 200, 10],
}

#生命药品:
life_durgs_dict = {
    #名称:[增加值,多少钱,库存]
    "小血瓶":[10, 100, 10],
    "中血瓶":[50, 150, 10],
    "大血瓶":[100, 200, 10],
}


#武器:
weapon_dict = {
    #名称:[攻击力,多少钱,库存]
    "青龙偃月刀":[100,1000,10],
    "丈八蛇矛":[100,1000,10],
    "双剑":[100,1000,10],
    "方天画戟":[150,2000,10],
}

samll_magic_bottle = Commodity("小魔瓶","魔法",magic_durgs_dict["小魔瓶"][0],
                               magic_durgs_dict["小魔瓶"][1],magic_durgs_dict["小魔瓶"][2])
middle_magic_bottle = Commodity("中魔瓶","魔法",magic_durgs_dict["中魔瓶"][0],
                               magic_durgs_dict["中魔瓶"][1],magic_durgs_dict["中魔瓶"][2])
big_magic_bottle = Commodity("大魔瓶","魔法",magic_durgs_dict["大魔瓶"][0],
                               magic_durgs_dict["大魔瓶"][1],magic_durgs_dict["大魔瓶"][2])


samll_life_bottle = Commodity("小血瓶","生命",life_durgs_dict["小血瓶"][0],
                               life_durgs_dict["小血瓶"][1],life_durgs_dict["小血瓶"][2])
middle_life_bottle = Commodity("中血瓶","生命",life_durgs_dict["中血瓶"][0],
                               life_durgs_dict["中血瓶"][1],life_durgs_dict["中血瓶"][2])
big_life_bottle = Commodity("大血瓶","生命",life_durgs_dict["大血瓶"][0],
                               life_durgs_dict["大血瓶"][1],life_durgs_dict["大血瓶"][2])


qinlong = Commodity("青龙偃月刀","武器",weapon_dict["青龙偃月刀"][0],
                               weapon_dict["青龙偃月刀"][1],weapon_dict["青龙偃月刀"][2])
shemao = Commodity("丈八蛇矛","武器",weapon_dict["丈八蛇矛"][0],
                               weapon_dict["丈八蛇矛"][1],weapon_dict["丈八蛇矛"][2])
shaungjian = Commodity("双剑","武器",weapon_dict["双剑"][0],
                               weapon_dict["双剑"][1],weapon_dict["双剑"][2])
huaji = Commodity("方天画戟","武器",weapon_dict["方天画戟"][0],
                               weapon_dict["方天画戟"][1],weapon_dict["方天画戟"][2])







