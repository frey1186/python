import sys
import time
import RoleClass
import role_and_scene
import random

def step_0():
    ################################ 背景 ###################################
    print("-"*50)
    print("-"*50)
    print("#"*15,"拯救女友","#"*15)
    print("-"*50)
    print("-"*50)

    print("正在加载...")
    for i in range(20):
        sys.stdout.write("#")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")

    #实例化me,游戏主角
    name = input("为你自己起个名字:")
    g_name = input("对了,你女朋友叫什么?:")
    life_value = 1000
    magic_value = 1000
    defend_value = 10
    attack_value = 20

    me = RoleClass.Me(name,life_value, magic_value, defend_value, attack_value)

    time.sleep(1)
    print("\n就在你给自己起名字的时候,你的女朋友%s被路过的金角大王和银角大王抓走啦...." % g_name)
    time.sleep(1)
    print("""\n我去,
赶紧行动起来吧,打败金角大王和银角大王,
不然,""")
    time.sleep(1)
    print("女友的就被O--O--X--X啦")
    while True:
        print("-"*50)
        continue_next_step = input("是否开始干金角大王? Y/N")
        if continue_next_step.strip().lower() == "y":
            return me
        elif continue_next_step.strip().lower() == "n":
            exit()
        else:
            print("wrong input..")



def step(me,guan=1):
    ################################ 第n关 ###################################
    print("-"*50)
    print("-"*50)
    print("#"*15,"第%s关" % guan,"#"*15)
    print("-"*50)
    print("-"*50)
    time.sleep(1)
    me.speak("站住,放开我的女朋友...")
    time.sleep(2)
    role_and_scene.jinjiao.speak("切,孩儿们,给我上去收拾了呀的")
    time.sleep(2)
    #生成敌人的顺序列表
    level_enemy_list = role_and_scene.scene_list2[guan-1]
    #并打印出来
    
    for k,v in role_and_scene.scene_list[guan-1].items():
        print("来了%s个%s..." % (v, k))

    while True:
        if len(level_enemy_list) >0:
            print("开始一轮攻击")

            #小喽喽们随机收到攻击,掉血
            index = random.randrange(len(level_enemy_list))
            level_enemy_list[index].be_attacked(me.attack())
            me.list_life()


            #如果某个小喽喽死了,就从列表中产出
            for enemy in level_enemy_list:
                if not enemy.is_live:
                    level_enemy_list.remove(enemy)

            print("敌人进攻啦....")
            #或者的敌人开始进攻
            for enemy in level_enemy_list:
                    me.be_attacked(enemy.attack())
            #查看我的生命值
            me.list_life()
            #如果死啦:
            if not me.is_live:
                role_and_scene.jinjiao.speak("二货,你女朋友是我的啦...哈哈哈")
                print(">>>>> GAME OVER.....")
                break


        else:
            if guan == 3:
                #第三关:
                role_and_scene.jinjiao.speak("woca,你牛逼,我死啦...")
                role_and_scene.jinjiao.speak("但是你的女朋友已经被我送给我三弟啦,有本事就去找他.....")
            elif guan == 2:
                #第二关:
                role_and_scene.jinjiao.speak("我的银角啊....")
                time.sleep(2)
            else:
                #第一关:
                role_and_scene.jinjiao.speak("woca,你牛逼,居然还没死...你等着")
                time.sleep(2)
            break



if __name__ == '__main__':
    #先运行背景
    me = step_0()
    for i in range(1,4):
        #逐关运行
        step(me, guan=i)

