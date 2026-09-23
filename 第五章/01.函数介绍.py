#函数: 函数是组织好的,可重复使用的,用来实现特定功能的代码片段
#函数基础:
#定义函数
# def 函数名(参数列表):
#     函数体
#     ......
#     return 返回值
#
# 函数名(参数)
# 函数使用的注意事项:
#     函数必须先定义,后调用
#     函数定义时,并不会执行,只有在调用函数时,函数体的逻辑才会运行
#     函数中通过缩进来描述归属关系
# def but_line():
#     print("===============")
#     print("===============")
#
# but_line()
#
# def pi(r):
#     area =3.14*r*r
#     return area
#
# print(pi(10))
#
# #计算长方形的面积
# def rectangle(x,y):
#     """
#     该函数用于计算长方形的面积
#     :param x: 长方形的长度
#     :param y: 长方形的宽度
#     :return: 长方形的面积
#     """
#     area=x*y
#     return area
# print(rectangle(10,20))
#
# #函数3:计算圆的面积,周长 --->半径--->如果返回值有多个,多个返回值之间逗号分隔--->多个返回值会封装到元组之中
# def circle_area_len(r):
#     """
#     该函数用于根据圆的半径,计算圆的面积和圆的周长
#     :param r: 圆的半径
#     :return: 圆的面积,圆的周长
#     """
#     return round(3.14*r*r,2),round(3.14*r*2,2)
#
# al = circle_area_len(10)
# print(al)
# print(type(al))
# print()
#
# area,len = circle_area_len(10)  #解包操作
# print(area)
# print(len)
#
# #函数的说明文档:是写在函数开头,用三个引号包裹的字符串,
# # 用于解释函数的功能而,参数,返回值等信息,方便调用者清除函数的具体操作及细节
# help(rectangle)
# help(circle_area_len)

