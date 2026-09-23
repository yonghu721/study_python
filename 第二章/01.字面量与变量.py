# 字面量的写法
# print(100) #整数
# print(3.14) #小数
# print(True) #布尔值
# print(False) #布尔值
# print("hello world") #字符串
# print("---------------") #字符串
# print(None) #空值(NoneType)
#
# #布尔类型本质属于整数类型(True = 1 ; False = 0)
# print(True + 1)
# print(False - 1)

#1. 什么是字面量?
# 程序中,直接书写的固定值(数据)

#2. 各个类型字面量的书写形式
# 整数(int):10,20;
# 小数/浮点数(float):3.14
# 字符串:双引号("人生苦短,我学python")
# 布尔(bool):True(真-1)/False(假-0);(首字母必须大写)
# 空值:(NoneType):None

# 学习进度--26年9月17日
# 黑马python 1-10集已学完


#变量-------python是动态语言,一个变量是可以存储不同类型的数据的
# (但是项目开发中,推荐变量只存储一种类型的数据)
# num = 1114.1
# print(num)
# num = 1114.2
# print(num)
# num= num +1
# num = 1114.2
# num = 'ok'
# print(num)
#
# num = 20.7
# num1 = 20.7+50
# num2 = num1 +50
# print("未来一个月的播放量为",num1,"未来两个月的播放量为",num2)
#
# base, incr = 20.7,50
# print(base+incr,base+incr+incr)
# a,b = 10,"python"
# print(a,b)

# #笔记:
# #1.什么是变量?如何定义?
# 在程序中变量是用来存储单个数据的容器(经常会发生改变的数据); num = 10
# #2.变量的使用?
# 输出打印/参与计算/记录数据
# #3.注意事项?
# 一个变量只能存储一个值
# 变量定义的时候只能赋值才可以使用
# 一条语句可以定义多个变量,也可以连续赋值(a,b = 10,"python")

#标识符

# true = 1
# print(true)
#
# a = 10
# b = 20
# c = a
# a = b
# b = c
# print(a,b)

a = 100;b = 200;c = 300;
#a b c = c a b = 300 100 200

d = a
a = c
c = d
d = b
b = c
c = d
print(a,b,c)

a,b,c = 100,200,300
a,b,c = c,a,b
print(a,b,c)

print(type(a),type(b))