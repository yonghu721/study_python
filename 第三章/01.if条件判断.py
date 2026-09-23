# score = 690
# if score >= 680:
#     print("清华欢迎您")
# else:
#     print("北大欢迎您")
from selectors import SelectSelector

# 1.if条件判断的基本格式
#     条件成立时,要执行对应的操作1
#     条件成立时,要执行对应的操作2

# 2. if语句的注意事项
#     判断条件的结果一定是布尔类型
#     不要忘记判断条件后的冒号
#     if语句里面的代码块,需要在前方缩进空格(建议4个空格),通过缩进来描述代码的层级关系(归属)

#需求:介个前面学习的输入输出以及if条件判断的知识,完成b站登录功能的实现(正确账号和密码为18888888888/666888).

# account = "18888888888"
# password = "666888"
# zh = input("请输入账号:")
# mm = input("请输入密码:")
# if zh == account and mm == password:
#     print(f"欢迎登录,账号{account}的用户")
# else:
#     print("账号或密码错误")

#if ... else 结构
# if 要判断的条件:
#     条件成立时,执行对应的操作1
# else:
#     条件不成立时,执行对应的操作2
#

# year = int(input("请输入一个4为数的年份:"))
# if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
#     print(f"{year}是闰年")
# else:
#     print(f"{year}不是闰年")

# 1. 根据用户输入的数字,判断该数字是奇数还是偶数
# num = int(input("请输入一个数字:"))
# if num % 2 == 0:
#     print(f"{num}是偶数")
# else:
#     print(f"{num}是奇数")

# 2. 根据用输入输入的年龄,判断该用户是否已经成年(>=18,成年;否则,未成年)
# age = int(input("请输入您的年龄:"))
# if age >=18:
#     print("成年")
# else:
#     print("未成年")

# 3. 根据用户输入的数字,判断该数字是正数还是负数(不考虑0)
# num = float(input("请输入一个数字:"))
# if num>0:
#     print(f"{num}为正数")
# elif num<0:
#     print(f"{num}为负数")
# else:
#     print(f"{num}为0")

# 4. 根据用户输入的考试分数,判断该分数是否及格了(大于等于60就是及格了)
# score = int(input("请输入您的考试分数"))
# if score >=60 and score <=150:
#     print("及格")
# else:
#     print("不及格")

# if语句进阶 - if... elif ... else
# 如果 数字>0 : 正数
# 如果 数字<0 : 负数
# 否则: 0

# accout = input("请输入用户名:")
# password = input("请输入密码:")
# if accout == "admin" and password == "666888":
#     print("欢迎用户admin登录成功")
# elif accout == "root" and password == "547527":
#     print("欢迎用户root登录成功")
# elif accout == "zhangsan" and password == "123456":
#     print("欢迎用户zhangsan登录成功")
# else:
#     print("用户或密码错误")

# score = int(input("请输入您的考试分数"))
# if score >=85:
#     print("优秀")
# elif score >=60 and score <85:
#     print("及格")
# else:
#     print("不及格")

# num = float(input("请输入商品的总额:"))
# if num >= 500:
#     num1 = num*0.8
#     print(f"{num1}")
# elif num >=300 and num < 500:
#     num2 = num*0.7
#     print(f"{num2}")
# elif num>=100 and num < 300:
#     num3 = num*0.95
#     print(f"{num3}")
# else:
#     print(f"{num}")

# 案例:三角形类型判断:根据输入的三个边的边长(正整数) 判定是等边三角形/等腰三角形/普通三角形,还是不能构成三角形.
#构成三角形的条件:两百年纸盒大于第三边
# 三角形判定规则:
#     三个边都相等:等边三角形
#     两个相等:等腰三角形
#     三个边都不相等:普通三角形

# a = int(input("请输入第一个边的边长:"))
# b = int(input("请输入第二个边的边长:"))
# c = int(input("请输入第三个边的边长:"))
# if (a+b>c and b+c>a and c+a>b) or (a-b<c and b-c<a and c-a<b):
#     print("符合构建三角形的条件")
#     if a == b and b == c:
#         print("等边三角形")
#     elif a == b or b == c or c == a:
#         print("等腰三角形")
#     elif a != b and b != c and c != a:
#         print("普通三角形")
# else:
#     print("不是一个三角形")

num = float(input("请输入您今年用过的电量°:"))
if num < 2880:
    num1 = num*0.4883
    print(f"今年已使用{num}°电,共计{num1}元")
elif num>=2880 and num<=4800:
    num2 = 2880*0.4883+(num-2880)*0.5383
    print(f"今年已使用{num}°电,共计{num2}元")
else:
    num3 = 2880*0.4883+(4800-2880)*0.5383 + (num-4800)*0.7883
    print(f"今年已使用{num}°电,共计{num3}元")