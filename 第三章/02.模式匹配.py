#模式匹配  match ... case
#结构模式匹配就是用一个清晰的模版去精准的匹配数据的结构和内容,匹配成功则执行相应的操作
#例子
# day = input("请输入星期几(1-7):")
# match day:
#     case "1":
#         print("周一")
#     case "2":
#         print("周二")
#     case "3":
#         print("周三")
#     case "4":
#         print("周四")
#     case "5":
#         print("周五")
#     case "6":
#         print("周六")
#     case "7":
#         print("周日")
#     case "8" | "9":
#         print("测试")
#     case _:
#         print("输入错误")

# 其中 | 表示或的关系,匹配多个模式中的任意一个; _ 表示匹配其他所有的情况
# num1 = float(input("请输入第一个数:"))
# num2 = float(input("请输入第二个数:"))
# oper = input("请输入需要运算的符号(+-*/):")
#
# match oper:
#     case "+":
#         print(num1+num2)
#     case "-":
#         print(num1-num2)
#     case "*":
#         print(num1*num2)
#     case "/" if num2 != 0: #if 条件成立,才匹配这个case
#         print(num1/num2)
#     case _:
#         print("运算符输入错误")

# 1. match...case 语法:
# match 表达式:
#     case 值1:
#         操作1
#     case 值2 if 条件表达式:
#         操作2
#     case 值3 | 值4:
#         操作3
#     case _:
#         操作默认
# 2. match...case应用场景
#    match:基于某个变量的多个 固定值 进行分支判断时,可以使用match模式匹配
#    if: 条件判断设计多个复杂的逻辑判定,范围比较及组合条件时
#

num = input("玩家输入的指令:")
match num:
    case "上" | "W" | "w":
        print("角色向上移动")
    case "下" | "S" | "s":
        print("角色向下移动")
    case "左" | "A" | "a":
        print("角色向左移动")
    case "右" | "D" | "d":
        print("角色向右移动")
    case "跳" | "":
        print("角色跳跃")
    case "攻击" | "J" | "j":
        print("角色发动攻击")
    case "退出" | "ESC" | "esc":
        print("角色退出游戏")
    case _:
        print("输入方式错误!!!")
