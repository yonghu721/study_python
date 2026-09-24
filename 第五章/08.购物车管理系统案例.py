#商品
import math


class Goods:
    def __init__(self,name,price,num):
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名称:{self.name},商品价格:{self.price},商品数量:{self.num},总价格:{self.price * self.num}"

    def updata_goods(self,name = None,price = None,num = None):
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num

#购物车系统
class ShoppingCart:
    system_version = "1.0.0"
    system_name = "购物车系统"

    def __init__(self):
        self.goods_list = []

    #添加物品成绩
    def add_goods(self):
        name = input("请输入物品名称:")

        for i in self.goods_list:
            if i.name == name:
                print("该物品已存在,不需要进行添加!")
                return
        price = int(input("请输入商品的价格:"))
        num = int(input("请输入商品的数量:"))

        goods = Goods(name,price,num)
        self.goods_list.append(goods)
        print("商品添加成功!")

    #修改商品
    def update_goods(self):
        name = input("请输入物品名称:")
        for i in self.goods_list:
            if i.name ==name:
                print(f"当前物品信息为:{i}")

                price = int(input("请输入修改后的价格:"))
                num = int(input("请输入修改后的数量"))

                i.updata_goods(name,price,num)
                print("修改成功~")
                print(f"修改后的信息为:{i}")
                return
        print("没有该商品,请重新输入!")

    #删除商品
    def delete_goods(self):
        name = input("请输入物品名称:")
        for i in self.goods_list:
            if i.name == name:
                self.goods_list.remove(i)
                print("物品删除成功!")
                return
        print("未找到该商品,删除失败")

    #展示商品
    def all_goods(self):
        for i in self.goods_list:
            print(i)

    #运行系统
    def run(self):
        print(f"欢迎使用{ShoppingCart.system_name}!当前版本为:V{ShoppingCart.system_version}")
        print()
        while True:
            print()
            print("==============================================================")
            print("1.添加购物车   2.修改购物车   3.删除购物车   4.查询购物车   5.退出系统")
            print("==============================================================")
            print()

            choice = int(input("请选择要执行的操作,输入1-5:"))
            match choice:
                case 1:
                    self.add_goods()
                case 2:
                    self.update_goods()
                case 3:
                    self.delete_goods()
                case 4:
                    self.all_goods()
                case 5:
                    print("Bye ~ Bye ~")
                    break
                case _:
                    print("选择错误,选择1-5")

if __name__ == '__main__':
    shopping_cart = ShoppingCart()
    shopping_cart.run()

