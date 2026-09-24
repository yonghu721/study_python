"""
面向过程编程
核心思想:把一个需求分解成一系列要执行的步骤,然后按照步骤一次执行这些任务(关注的是流程,步骤).
面向对象编程
  对象可以理解为现实中具体的人/物在程序中的数字化身(万物皆对象)
  他把一个人/物的特征(属性)和功能(方法)打包到一起,是面向对象编程的基本单元.
  关注的是谁来帮我做这件事

类与对象
类:描述的是一组句偶相同属性(特征)和方法(功能/行为)的模版
对象: 对象是类的实例,是基于类创建出来的(实例对象)
对象是由类创建出来的,创建对象的过程,也称为对象的实例化.一个类可以创建无数个对象.
"""
#定义类
"""
class 类名:
    pass
#创建对象
对象名 = 类名()
对象名.属性名1 = 属性值1
对象名.属性名2 = 属性值2
"""

#定义类  --->  不推荐,不便于管理和维护
# class Car:
#     pass
#
# #创建对象
# c1 = Car()
# #动态的为对象添加属性
# c1.color = "red"
# c1.brand = "BMW"
# c1.name = "X5"
# c1.price = 500000
#
# print(c1.color)
# print(c1)
# print(c1.__dict__) # 会将对象中的属性以字典的形式输出出来

#推荐写法
"""
#定义类
class 类名:
    def __init__(self,参数列表):
        self.属性名 = 参数值
        self.属性名 = 参数值
        #self:方法的第一个参数,表示当前创建的实例对象
#创建对象
对象名 = 类名(参数列表)
#定义在类外面成为函数,定义在类中的函数称之为方法.
#__init__:初始化方法,对象创建后自动调用,主要用于设置对象的初始化状态(设置对象属性)

"""

# class Car:
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.c_color = c_color
#         self.c_brand = c_brand
#         self.c_name = c_name
#         self.c_price = c_price
#         print("Car 类型的对象初始化完毕,对象属性已经完成添加")
#         print(f"{self.c_color},{self.c_brand},{self.c_name},{self.c_price}")
#
# c1 = Car("红色","宝马","E300",500000)
# print(c1.__dict__)
#
# s2 = Car("白色","奔驰","X7",800000)
# print(s2.__dict__)

#9.23=71-78
#----------------------------------------实例方法-------------------------------------

"""
#定义类
class 类名:
    def __init__(self,参数列表):
        self.属性名 = 参数值
        self.属性名 = 参数值

    def 方法名(self,形参列表):
        ...
    def 方法名(self,形参列表):
        ...
#创建对象
对象名 = 类名(参数列表)
对象名.方法名(实参)

"""

# class Car:
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.c_color = c_color
#         self.c_brand = c_brand
#         self.c_name = c_name
#         self.c_price = c_price
#         print("Car 类型的对象初始化完毕,对象属性已填加完毕 .")
#
# #定义实例方法
#     def running(self):
#         print(f"{self.c_brand} {self.c_name}正在高速行驶中...")
#
#     def total_cost(self,discount,rate):
#         """
#         计算提车的总费用,包含两个部分:车的价格,税费
#         :param discount: 折扣
#         :param rate: 税率
#         :return: 提车的费用
#         """
#         total_cost = self.c_price * discount + rate * self.c_price
#         return total_cost

#测试
# c1 = Car("red","BMW","X7",800000)
# c1.running()
# print(c1)
# total_price = c1.total_cost(0.9,0.05)
# print("提车的费用为:",total_price)

#----------------------------魔法方法-----------------------------------------

"""
#魔法方法是指python中提供的双下划线开头和结尾的特殊方法,用于定义类的特殊行为,比如:__init__
#不需要手动调用,python会在合适的时机自动调用
    __init__:初始化方法
    __str__:字符串表示的方法
    __eq__:比较两个对象是否相等(equal)
    __lt__,__le__,__gt__,__ge__:支持比较两个对象的大小
    (小于-lt-<,小于等于-le-<=,大于-gt->,大于等于-ge->=)
    

"""

# class Car:
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.c_color = c_color
#         self.c_brand = c_brand
#         self.c_name = c_name
#         self.c_price = c_price
#         print("Car 类型的对象初始化完毕,对象属性已填加完毕 .")
#
# #定义实例方法
#     def running(self):
#         print(f"{self.c_brand} {self.c_name}正在高速行驶中...")
#
#     def total_cost(self,discount,rate):
#         """
#         计算提车的总费用,包含两个部分:车的价格,税费
#         :param discount: 折扣
#         :param rate: 税率
#         :return: 提车的费用
#         """
#         total_cost = self.c_price * discount + rate * self.c_price
#         return total_cost
#
#     def __str__(self):
#         return f"{self.c_color},{self.c_brand},{self.c_name},{self.c_price}"
#     def __eq__(self,other):
#         return self.c_color == other.c_color and self.c_brand == other.c_brand and self.c_name == other.c_name and self.c_price == other.c_price
#     def __lt__(self,other):
#         return self.c_price < other.c_price
#
# c1 = Car("白色","BYD","X7",300000)
# c2 = Car("白色","BYD","X7",500000)
# print(c1)
# print(c2)
# print(c1 == c2)
# print(c1.c_price < c2.c_price)
# print(c1 < c2)

#--------------------------------实例属性和类属性---------------------------------------
"""
    实例属性:属于每一个具体对象的属性,每个对象都是独立的.(各个对象特有的数据)
    类属性:类属性是属于类本身的属性,所有实力共享的.(所有对象共享的数据或配置)
    self.brand = c_brand
    实例属性(通过 实例对象.属性 的方式操作)
    wheel = 4 #轮胎的数量
    tax_rete = 0.1 #购置税
    类属性(通过 类名.属性 的方式操作)
"""

class Car:
    #类属性 (所有实例对象共享的)
    wheel = 4 #轮胎的数量
    tax_rete = 0.1 #购置税的税率
    def __init__(self,c_color,c_brand,c_name,c_price):
        #实例属性
        self.c_color = c_color
        self.c_brand = c_brand
        self.c_name = c_name
        self.c_price = c_price
        self.wheel = 4
        print("Car 类型的对象初始化完毕,对象属性已填加完毕 .")

#定义实例方法
    def running(self):
        print(f"{self.c_brand} {self.c_name}正在高速行驶中...")

    def total_cost(self,discount,rate):
        """
        计算提车的总费用,包含两个部分:车的价格,税费
        :param discount: 折扣
        :param rate: 税率
        :return: 提车的费用
        """
        total_cost = self.c_price * discount + rate * self.c_price
        return total_cost

c1 = Car("白色","BYD","X7",300000)
print(c1.c_brand)
print(c1.wheel) #通过实例对象,查找属性时,会先查找实例属性;当实例属性不存在在查找类属性

#通过类名访问类属性
print(Car.wheel,Car.tax_rete)


# c2 = Car("白色","BYD","X7",500000)
# print(c2)

