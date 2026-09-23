
shopping_cart = {}
menu = """
#########购物车系统###########
#       1.添加购物车         #
#       2.修改购物车         #
#       3.删除购物车         #
#       4.查询购物车         #
#       5.退出购物车         #
############################
"""

print("欢迎使用购物车管理系统!")

while True:
    # 1.制作菜单
    print(menu)
    choice = input("请选择需要执行的操作(1-5):")

    # 2.执行的具体操作
    match choice:
        case "1":  # 添加购物车
            name = input("请输入商品的名称:")
            price = float(input("请输入商品的价格:"))
            quantity = int(input("请输入商品的数量:"))

            if name in shopping_cart:
                print("该商品已存在,请重新选择要添加的商品!")
            else:
                shopping_cart[name] = {"价格": price, "数量": quantity}
                print("商品添加完毕~")
                print(shopping_cart)

        case "2":  # 修改购物车
            name2 = input("请输入您需要修改的商品名称:")
            if name2 not in shopping_cart:
                print("该商品不存在,无法修改,请重新选择要修改的商品!")
            else:
                price2 = input("请输入您需要修改的商品价格:")
                quantity2 = input("请输入您需要修改的商品数量:")
                shopping_cart[name2] = {"价格": price2, "数量": quantity2}
                print("商品修改完毕~")
                print(shopping_cart)

        case "3":  # 删除购物车
            name3 = input("请输入您需要删除的商品:")
            if name3 not in shopping_cart:
                print("改商品不存在,无法删除,请重新选择!!")
            else:
                del1 = shopping_cart.pop(name3)
                print(f"商品{del1}以删除")

        case "4":  # 查询购物车

            for name in shopping_cart.keys():
                info = shopping_cart[name]
                print(f"商品名称:{name},商品价格{info["价格"]},商品数量{info["数量"]}")

        case "5":  # 退出购物车
            print("欢迎下次使用,拜拜!")
            break
        case _:  # 匹配其他所有情况
            print("非法操作,不支持!!!")

