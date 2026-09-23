#猜数字游戏
# 1. 系统随机生成一个随机数
# 2. 用户根据提示猜数字,并将所猜的数字输入系统
# 3. 如果猜错了,系统会给出提示是猜大了,还是猜小了,然后继续输入猜的数字
# 4. 如果猜对了,系统自动退出,游戏结束

#生成随机数
# import random
#
# random_number = random.randint(1,100)
# while True:
#     num = input("这个数字在1-100之间,请输入你的猜测:")
#     if num =="" :
#         print("禁止为空,请输入猜测的数字")
#         continue
#     num = int(num)
#
#     if num == random_number:
#         print(f"猜测正确,随机数为{random_number}")
#         break
#     elif num > random_number:
#         print("猜大了")
#
#     elif num < random_number:
#         print("猜小了")
#
# sum = 0
# for i in range(1,1001):
#     if i % 5 == 0:
#         sum += i
# print(f"1-1000所有5的倍数累加起来为:{sum}")

str123 = input("请输入一个随机的字符串:")
a = 0
k = 0
for i in range(0,len(str123)):
    if str123[i] == "a":
        a+=1
    elif str123[i] == "k":
        k+=1
print(f"字符串中a的个数有{a}个,k的个数有{k}个")
