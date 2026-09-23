# input--从键盘上输入
# print--输出
#--从键盘当中无论输入的是什么数据,最后获取到的都是字符串,所有键盘获取的数据都是字符串
from idlelib.window import add_windows_to_menu

# a = input('请输入变量')
# print(a)
#
# name = input("请输入您的姓名:")
# print(f"欢迎你,{name}")
# age = input("请输入您的年龄:")
# print(f"您今年{age}岁")

# atm = 10000
# mima = input("请输入密码:")
# print("密码正确")
# num =input("请输入取款金额:")
# atm = atm - int(num)
# print(f"您的银行卡还剩{atm}元")

# 其他类型转为int类型:int()
# 其他类型转为str类型:str()
# 其他类型转为float类型:float()
# 其他类型转为bool类型:bool()


#需求:根据用户输入的两个数字,计算两个数之和,并将其输出到控制台.
a = input ("请输入第一个数字:")
b = input("请输入第二个数字:")
c = int(a)+int(b)
print(f"第一个数字为:{a},第二个数字为:{b},他们的和是:{c}")

