#打印一个长度为m,宽度为n的长方形
# m = int(input("请输入长方形的长度:"))
# n = int(input("请输入长方形的宽度:"))
# #print("*"):自带换行效果,每一次执行都会输出新的一行;
#
# #end = " " 表示的是每一次输出以什么结束;默认 /n
# for j in range(n):
#     for i in range(m):
#         print("*",end="  ")
#     print("\n")

#案例 打印99乘法表
# for i in range(1,10 ):
#     for j in range(1,i+1):
#         print(f"{j} * {i} =", i * j, end="\t")
#
#     print()

#需求1. 根据输入的直角边的边长,打印等腰直角三角洲(如下位直角边为5的等腰直角三角形)
# num = int(input("请输入直角边的边长:"))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print("*",end = "  ")
#     print()

#需求2. 根据输入的数字,打印对应的数字金字塔
# num = int(input("请输入需要打印的数字:"))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(f"{j}",end = "  ")
#     print()

#需求3. 打印国际象棋棋盘
# ■□
for i in range(1,9):
    for j in range(1,9):
        if (i+j)%2==1:
            print("□",end="  ")
        else:
            print("■",end="  ")
    print()





