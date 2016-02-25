import RoleClass

loulou = RoleClass.Minions("小喽喽",150,10,1)
jinjiao = RoleClass.Boss("金角大王",1000,100,10,100)
yinjiao = RoleClass.Boss("银角大王",900,90,8,50)

#场景

scene_list = [
    #{来攻敌人:数量,},{...}
    {#第一关
        "小喽喽":3,
    },
    {#第2关
        "小喽喽":3,
        "银角大王":1
    },
    {#第3关
        "小喽喽":5,
        "金角大王":1,
    },
]

# #敌人定义:实例化每个敌人,并将每关卡的敌人放入列表中[[第一关敌人],[第二关敌人],[第三关敌人]]
scene_list2 = []
for k,v in enumerate(scene_list):
    scene_list2.append([])
    for keys in v:
        if keys == loulou.name:
            for i in range(v[keys]):
                scene_list2[k].append(RoleClass.Minions("小喽喽",200,10,1))
        if keys == jinjiao.name:
            for i in range(v[keys]):
                scene_list2[k].append(jinjiao)
        if keys == yinjiao.name:
            for i in range(v[keys]):
                scene_list2[k].append(yinjiao)





