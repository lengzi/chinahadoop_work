# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 上午12:40
# @Author  : lenzi
# @Site    : https://github.com/lengzi/
# @File    : chinahadoop_mall.py
# @Python  : python3.6 chinahadoop_mall.py
# @Software: PyCharm

goods_dict = {

    "001": {"name": "MacBookPro", "price": 14999},
    "002": {"name": "欧米茄手表 ", "price": 11111},
    "003": {"name": "小米笔记本 ", "price": 4999},
    "004": {"name": "Ipadmini2 ", "price": 1998},
    "005": {"name": "小米8手机  ", "price": 2998},
    "006": {"name": "爱马仕腰带 ", "price": 1999},
    "007": {"name": "劳力士男表 ", "price": 19999},
    "008": {"name": "巴宝莉眼镜 ", "price": 4999},
    "009": {"name": "路虎发现四 ", "price": 99999},
}



def print_goods_list(goods_list_dict):
    print("-----------欢迎进入小象购物商城-------------")
    print("商品编号","\t\t\t","商品名称","\t\t\t","商品价格")
    for num in sorted(goods_list_dict):
        print(num,"\t\t\t",goods_list_dict[num]["name"],"\t\t\t",goods_list_dict[num]["price"])

def buy_guide():
    print("请输入商品编号，购物完毕清输入q：")

def in_list(n,list):
    for num in list:
        if n == num:
            return True
    return False

def bye_message():
    print("谢谢使用小象购物商城，欢迎再次光临！")

def print_cart(shop_cart):
    print("您好！你购置得物品如下：")
    print("商品编号", "\t\t\t", "商品名称", "\t\t\t", "商品价格", "\t\t\t", "商品数量", "\t\t\t", "商品总价")
    for num in shop_cart:
        print(num,"\t\t\t",shop_cart[num]["商品名称"],"\t\t\t",shop_cart[num]["商品单价"],"\t\t\t",shop_cart[num]["商品数量"],"\t\t\t",shop_cart[num]["商品总价"])


def compute_price(shop_cart):
    money = 0
    for num in shop_cart:
        money += (int)(shop_cart[num]["商品总价"])
    return money




def main():
    print_goods_list(goods_dict)
    #buy_guide()
    cart = {}
    flag1 = "请输入商品编号,结束购物请输入q:"
    flag2 = "请输入购买商品的数量："
    flag = flag1
    key = input(flag)
    cart_num = 0
    while key:
        if key == "q":
            if not cart:
                bye_message()
            else:
                print_cart(cart)
                cash = compute_price(cart)
                print("购物愉快！请支付金额",cash,"元：")
                my_cash = input()
                while my_cash:
                    if not my_cash.isnumeric():
                        print("请输入正确的数字：")
                        my_cash = input()
                    elif int(my_cash) < cash:
                        print("您支付的金额不足，清重新输入：")
                        my_cash = input()
                    else:
                        break
                if int(my_cash) == cash:
                    print("支付成功！欢迎下次光临")
                else:
                    print("支付成功！找给你",int(my_cash)-cash,"元，欢迎下次惠顾！")
            break

        else:
            print_goods_list(goods_dict)
            if not in_list(key,goods_dict) and flag == flag1:
                print("商品编号不存在，请重新输入：")
                print_goods_list(goods_dict)
                key = input(flag)
            elif in_list(key,goods_dict):
                cart_num = key
                flag = flag2
                key = input(flag2)
            elif not key.isnumeric():
                print("请输入数字：")
                key = input()
            else:
                if int(key)>0:
                    a = int(key)
                    if cart_num in cart.keys():
                        a += cart[cart_num]["商品数量"]
                    cart[cart_num] = {"商品名称": goods_dict[cart_num]["name"], "商品单价": goods_dict[cart_num]["price"], "商品数量":int(a), "商品总价": goods_dict[cart_num]["price"]*int(a)}

                    print("你的购物车清单如下：")
                    print_cart(cart)
                    print_goods_list(goods_dict)
                    flag = flag1
                    print("继续购物，请输入商品编号，结束购物请输入q：")
                    key = input()
                else:
                    print("商品数量不能为0,请重新输入：")
                    key = input()



if __name__ == '__main__':
    main()
