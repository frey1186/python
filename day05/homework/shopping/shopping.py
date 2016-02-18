import  json
product_list_file = "shopping/product_list.txt"


def get_product():

    """

    :param menu_dict: 多级菜单，这里先弄一级菜单，回头有时间再改
    :return:返回产品列表，格式为 [产品,单价，数量]

    """
    menu_dict = {
        "苹果": 5,
        "iphone": 5000,
        "ipad": 2998,
        "iwatch": 3000,
        "地瓜": 2,
        "榴莲": 18,
    }
    menu_list = []
    product_list = []
    while True:
        for i, k in enumerate(menu_dict):
            print("%d\t%s\t\t%s元"% (i, k, menu_dict[k]))
            menu_list.append([k,menu_dict[k]])
        input_str = input("输入您的选择：（Q：退出）")
        if input_str.strip().lower() == "q":
            break
        elif input_str.strip().isdigit():
            menu_index = int(input_str.strip())
            if menu_index in range(len(menu_list)):
                product_list.append(menu_list[menu_index][0])
                product_list.append(menu_list[menu_index][1])
                input_count = input("输入购买数量：")
                if input_count.strip().isdigit():
                    product_list.append(int(input_count.strip()))
                else:
                    print("输入错误")
                    product_list.pop(menu_list[menu_index])
                break
            else:
                print("输入错误。")
        else:
            print("输入错误。again")

    return product_list



def shopping():
    try:
        fr = open(product_list_file, "r")
        product_list = json.load(fr)
        fr.close()
    except:
        product_list = [get_product()]
    while True:
        input_str = input("是否继续购物？（Y/N?）")
        if input_str.strip().lower() == "y":
            product_list.append(get_product())
        elif input_str.strip().lower() == "n":

            fw = open(product_list_file, "w")
            json.dump(product_list, fw)
            fw.close()
            #return product_list
            break

    #合并重复项
    for product in product_list:
        pass









# shopping(product_list_file)
# fr = open(product_list_file, "r")
# a = json.load(fr)
# fr.close()
# print(a)
