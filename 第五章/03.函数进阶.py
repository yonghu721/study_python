#函数 - 变量的作用域
#变量的作用域指的是变量的作用范围(标识这个变量在哪里可以使用,在哪里不可以使用).

# #global关键字:global用于明确的告诉Python解释器,在函数中要使用全局变量,使得可以在函数内部修改全局变量的值
# num = 1
# def func():
#     global num
#     num = 1000
#     print(num)
#
# func()
# print(num)

#------------------------------函数传参方式------------------------------------------
# 方式一:位置传参---常规
#调用函数时参数顺序与定义函数时参数顺序完全一致

# 方式二:关键字传参
#调用函数时以函数定义时形参名称作为关键字,以"键=值"的形式来传递参数(不要求顺序)
# def rg_stu(name,age,gender,city):
#     print(name,age,gender,city)
#     return name,age,gender,city
#
# stu = rg_stu(name="张三",age = 18,gender = "男",city="北京")
# print(stu)

#适用场景
#一切以代码结构清晰明了(可读性),便于维护(可维护性)为目标.
#如果参数比较少(不超过3个),可直接使用位置参数
#如果参数数量较多,建议使用关键字参数.

#---------------------------------默认参数---------------------------------

wenben = '''
默认参数也称为缺省参数,用于在定义函数时,为参考提供 默认值 ,
调用函数时,可以不传递有默认值的参数.
    可以在定义函数的时候为一个参数设置一个默认值
    例如:def reg_stu(name,age,city,gender="男"):
    这里的gender="男"就是默认值,或者叫做缺省参数
    注意事项:默认参数必须放在没有默认值的参数列表的后面,一个函数在定义时是可以设置多个默认值的

'''

# def reg_stu(name,age,city,gender="男"):
#     print(f"姓名{name},年龄:{age},地点:{city},性别:{gender}")
#     return name,age,city,gender
#
# stu = reg_stu("张三",18,"北京")
# print(stu)
# stu = reg_stu("王三",19,"北京","女")
# print(stu)

#---------------------------不定长参数(位置参数)------------------------------------
#不定长参数也可叫可变参数,用于函数定义及调用时参数个数不确定(0个或多个)的场景.

#不定长参数 - 位置传递( *args ),这些参数会合并风张伟一个元组
#args只是约定俗成的变量名,并不是关键字,这里可以使用任何合法的变量名(如:*data)
# def calc_data(*args):
#     """
#     根据传入的数据,计算数据的最小值,最大值,平均值
#     :param args: 传入的数据
#     :return: 最小值,最大值,平均值
#     """
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#     return {"最小值":min_data,"最大值":max_data,"平均值":round(avg_data,2)}
#
# data = calc_data(10,20,50,30,504,45,78,65,89,45)
# print(data)

#----------------------------不定长参数-关键字传递 **kwargs----------------------------
#关键字传递( **kwargs )
#参数以"键=值"形式传递的关键字参数,这些"键=值"参数都会被kwargs接受,并合并封装为一个字典类型
#*args 适用于处理数量不确定的数据
#**kwargs 适用于处理储量不确定的选项(函数的配置参数,用来指定函数的行为)

# def calc_data(*args,**kwargs):
#     """
#     根据传入的数据,计算数据的最小值,最大值,平均值
#     :param args: 传入的数据
#     :return: 最小值,最大值,平均值
#     """
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#
#     if kwargs.get("round") is not None: #不为none就是not none 这里判断这个元组获取的value不为none
#         #如果我拿到了round(round=xxx)参数,就执行if里面的代码;没有传round参数(拿到None),就跳过if里面的代码
#         avg_data = round(avg_data, kwargs.get("round"))
#     if kwargs.get("print"):
#         print(f"计算出来的最小值:{min_data},最大值:{max_data},平均值:{avg_data}")
#     return min_data,max_data,avg_data
#
# data = calc_data(10,20,50,30,504,45,78,65,89,45,round = 2,print=True)
# print(data)

#-------------------------------------参数的类型------------------------------------
#普通参数:数字,布尔,字符串,列表,元组,结合,字典,等
#特殊参数:函数
# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def calc(x,y,oper):
#     return oper(x,y)
#
# result = calc(10,20,add)
# print(result)

#------------------------------------匿名函数------------------------------------------
#匿名函数是没有名称的函数,需要通过lambda表达式来声明函数,可以简化简单函数的编写
#lambda 参数列表 : 函数体
#匿名函数的使用场景:函数逻辑比较简单并且只在一个场景使用时,可以考虑匿名函数来简化书写
# (通常作为高阶函数的参数使用)
#
# demo0 = lambda : print("------------")
# demo1 = lambda x,y:x+y
#
# demo0()
# print(demo1(10,20))

#需求:完成如下列表的排序操作,按照每一个元素的字符个数,从小到大排序;
# data_list = ["C++","C","Python","Java","Jack","Go","JavaScript","Rust"]
#
# data_list.sort(key=lambda item:len(item),reverse=True)
# 解析:排序的时候,不直接拿item本身比较大小,而是拿key函数返回的值当做"比较依据"
# 含义:把data_list列表中的元素,按照每一个元素的长度,从小到大排序
# print(data_list)
#
# data_list.sort(key=lambda item:len(item))
# print(data_list)
#
# num = lambda it:len(it)
#
# print(num(["C++","C","Python","Java","Jack","Go","JavaScript","Rust"]))

#------------------------案例---------------------------------------
#案例1. 计算n的阶乘
#递归调用(先层层递进,在逐层回归):指的是在函数中自己调用自己的情况 ---> 一定得有终结点
"""
jc(10) = 10 * jc(9)
jc(9) = 9 * jc(8)
jc(8) = 8 * jc(7)
jc(7) = 7 * jc(6)
jc(6) = 6 * jc(5)
jc(5) = 5 * jc(4) = 5 * 24 = 120
jc(4) = 4 * jc(3) = 4 * 6 = 24
jc(3) = 3 * jc(2) = 3 * 2 = 6
jc(2) = 2 * jc(1) = 2 * 1 = 2
jc(1) = 1

"""
# def jc(n):
#     if n == 1:
#         return 1
#     else:
#         return n*jc(n-1)
# result = jc(10)
# print(result)


#-------------------------------案例2-------------------------------------------
#电商订单计算器
#订单总金额 = 商品总金额 - 优惠卷 - 积分抵扣 + 运费
def calc_order_cost(*agrs,coupin,score,express):
    """
    根据传入的一批商品信息(商品名,价格,数量),优惠(优惠卷,积分抵扣),运费信息计算订单的总金额
    :param agrs:商品信息(商品名,价格,数量)--->如("鼠标",159,1),("键盘",299,2)
    :param coupin:优惠卷
    :param score:积分
    :param express:运费
    :return:
    """
    #1. 计算商品总金额
    total_price = [i[1]*i[2] for i in agrs]
    total_cost = sum(total_price)
    #2. 扣减优惠卷
    if total_cost >= 5000 and total_cost >=coupin:
        total_cost -= coupin
    #3. 扣减积分抵扣
    if total_cost >=5000 and total_cost >= score // 100:
        total_cost -= score // 100
    #4. 增加运费
    total_cost += express
    return total_cost

print(calc_order_cost(("鼠标",188,1),("电脑",7880,2),("耳机",235,1),("键盘",288,2),coupin=150,score=8000,express=9.9))

# 9.22=63-70







