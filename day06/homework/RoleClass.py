import settings

class Minions(object):  #爪牙
    """
    角色最高层类,也是爪牙类,即属性最少的角色
    """

    def __init__(self, name, life_value, defend_value, attack_value,is_live=True):
        self.name = name    #名字
        self.life_vaule = life_value  #生命值
        self.defend_value = defend_value  #防护值
        self.attack_value = attack_value  #攻击力
        self.is_live = is_live  #是否活着

    def speak(self,something):  #聊天
        """
        说话的函数
        :param something: 说话的内容
        :return: 无
        """
        print("[%s]:%s" % (self.name,something))

    def be_attacked(self,attack_value_of_enemy):  #被攻击
        """
        被攻击的函数
        :param attack_value_of_enemy: 被攻击损失血量
        :return: 无
        """
        self.life_vaule -= attack_value_of_enemy
        if self.life_vaule <= 0:
            self.is_live = False
            print("%s挂啦..." % self.name)
        else:
            print("%s被攻击了，掉了%s滴血。" % (self.name, attack_value_of_enemy))

    def attack(self):  #普通攻击
        """
        普通攻击函数
        :return: 攻击力
        """
        return self.attack_value

    def list_life(self):
        '''
        查看生命值的函数
        :return: 无
        '''
        print("[%s]生命:%s," %(self.name,self.life_vaule),end="")

class Me(Minions):  #我
    """
    主人公类,包含主人公所有方法
    """

    def __init__(self, name,life_value,magic_value,defend_value,attack_value,money=10000,level=1):
        super(Me,self).__init__(name,life_value,defend_value,attack_value,is_live=True)
        self.magic_vaule = magic_value  #魔法值
        self.money = money  #钱
        self.level = level  #级别
        self.experience = 0  #经验
        self.bag = []  #背包
        self.skills = [settings.skill_list[0]]

    def level_up(self):  #升级
        """
        检验是否应该升级的函数
        :return: 无
        """
        exp_list = settings.leve_and_experience_list[self.level]
        if self.experience >= exp_list[0] and self.experience < exp_list[1]:
            self.level += 1
            self.skills.append(settings.skill_list[self.level-1])


    def buy_something(self,something,price):
        """
        买东西的函数,放入背包中
        :param something: 商品
        :param price: 价格
        :return:
        """
        self.money -= price
        self.bag.append(something)

    def list_bag(self):
        """
        列举背包中的东西的函数
        :return: 无
        """
        if self.bag == []:
            print("你的背包是空的.")
        else:
            for i,v in enumerate(self.bag):
                print("%s\t%s" % (i,v))

    def take_magic_drugs(self,vaule_add_of_drugs):
        """
        吃魔法药水
        :param vaule_add_of_drugs: 增加魔法的量
        :return: 魔法值
        """
        self.magic_vaule += vaule_add_of_drugs

    def take_life_drugs(self,vaule_add_of_drugs):
        """
        吃血药
        :param vaule_add_of_drugs: 增加血的量
        :return: 生命值
        """
        self.life_vaule += vaule_add_of_drugs

    def attack_normal(self):  #普通攻击
        """
        普通攻击
        :return:
        """
        print("我打。")
        self.experience += self.attack_value
        self.level_up()
        return self.attack_value

    def list_skills(self):
        """
        列举所有技能
        :return:
        """
        print("%s\t%s" % (0,"普通攻击"))
        for i,v in enumerate(self.skills):
            print("%s\t%s" % (i+1, v[0]))

    def attck_with_magic(self, attck_vaule_with_magic, magic_dec):
        """
        魔法攻击
        :param attck_vaule_with_magic: 攻击力
        :param magic_dec: 魔法损耗
        :return: 总攻击力
        """
        if self.magic_vaule >= magic_dec:
            self.magic_vaule -= magic_dec
            self.experience += attck_vaule_with_magic*self.level*0.5
            self.level_up()
            return attck_vaule_with_magic*self.level
        else:
            print("魔法不够啦...")
            return 0

    def attack(self):
        """
        攻击函数
        :return: 攻击力值
        """
        self.list_skills()
        choose = input("输入你的选择:")
        if choose.strip().isdigit():
            if int(choose) in range(len(self.skills)+ 1):
                if int(choose) == 0:
                    return self.attack_normal()
                else:
                    skill_ability = settings.skill_list[int(choose)-1]
                    return self.attck_with_magic(skill_ability[1],skill_ability[2])

            else:
                print("wrong input")
                return 0
        else:
            print("wrong input")
            return 0





    def list_life(self):
        """
        列举生命值等
        :return:
        """
        print("[%s]生命:%s,魔法:%s,经验:%s,级别:%s" % (self.name,self.life_vaule,
                                               self.magic_vaule,self.experience,self.level))

class Boss(Minions):  #boss
    """
    大王的类,主要为金角和银角大王准备
    """

    def __init__(self, name,life_value,magic_value,defend_value,attack_value):
        super(Boss,self).__init__(name,life_value,defend_value,attack_value)
        self.magic_vaule = magic_value  #魔法值

    def attck_with_magic(self, life_dec, magic_dec):
        """
        魔法攻击
        :param life_dec:攻击力
        :param magic_dec: 魔法损耗
        :return: 攻击力
        """
        self.magic_vaule -= magic_dec
        return life_dec

    def list_life(self):
        """
        列举生命值等
        :return:
        """
        print("[%s]生命:%s,魔法:%s," % (self.name,self.life_vaule,self.magic_vaule))#
