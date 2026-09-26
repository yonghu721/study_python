#异常
#1. 不做处理:整个程序因为一个bug,中断执行.
#2. 捕获异常:按照我们自己的处理方式,处理完异常,程序继续执行.
"""
try:
    可能出现异常的业务代码1
    可能出现异常的业务代码2

except [异常类型 as 变量名]:
    出现异常时的预案
finally:
    不管是否出现异常,都会执行的代码

"""
# try:
#     print("===============================")
#     print(my_name)
#     print("===============================")
# except NameError as e: #捕获的是NameError 类型的异常
#     print(f"程序运行出错了,请联系管理员!异常信息为:{e}")

# try:
#     print("===============================")
#     # print(my_name)
#     # print(1/0)
#     # print("ABC"[10])
#     print("BCD".hello)
#     print("===============================")
# except NameError as e: #捕获的是NameError 类型的异常
#     print("名字不存在,请检查变量们或函数,异常信息:",e)
# except ZeroDivisionError as e:
#     print("0不能做被除数,异常信息:",e)
# except IndexError as e:
#     print("索引错误,异常信息为:",e)
# except Exception as e:
#     print("程序出错了,请联系管理员!异常信息为:",e)
# finally: #吴鸾程序是否正常运行,finally代码块中的代码都会运行
#     print("释放资源~")

#===================================异常的传递==========================================
# 异常传递就是异常在函数调用中层层上报的过程,直到处理他,或者程序崩溃.

def fun1():
    print("fun1---runninng---")
    fun2()

def fun2():
    print("fun2---runninng---")
    fun3()

def fun3():
    print("fun3---runninng---")
    print(my_name)

if __name__ == '__main__':
    try:
        fun1()
    except Exception as e:
        print("程序报错,请联系管理员,报错信息为:",e)
