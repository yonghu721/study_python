#字典:使用键值对(key:value) 来存储数据,每一个键都对应一个值,通过键(key)可以快速找到对应的值(value)
#特点:键值对(key:value)存储,键不能重复,可修改.
#定义:字典 -- key不能重复(如果重复,后面的值,会覆盖前面的值),key必须得是不可变类型(str,int.float,tuple),不能是list,set,dict
    #字典名称 = {key:value,key:value,...}
#定义空字典
    #字典名称 = {}
    #字典名称 = dict()
#根据key获取value
    #值 = 字典名称[key]
dict1 = {"王林":670,"韩立":556}
# print(dict1)
# print( dict1["王林"]) #获取
# #修改值
# dict1["王林"] = 888   #修改
# print(dict1)
# dict1["张三"] = 668
# print(dict1)

for item in dict1.items():
    print(item)

for k,v in dict1.items():
    print(k,v)
for i in dict1.keys():
    print(f"{i}:{dict1[i]}")