product_dict_file = "shopping/product_dict.txt"
from user import file_manage


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



def shopping(user, product_dict = {}):
    """

    :param user: 用户
    :param product_dict: 已购产品清单
    :return: 返回写入购物字典文件
    """
    try:

        product_dict = file_manage.file_read(product_dict_file)
        if not product_dict.get(user):
            product_dict[user] = [get_product(),]
    except:
        product_dict[user] = [get_product(),]

    while True:
        input_str = input("是否继续购物？（Y/N?）")
        if input_str.strip().lower() == "y":
            product_dict[user].append(get_product())
        elif input_str.strip().lower() == "n":

            file_manage.file_write(product_dict, product_dict_file)
            break

