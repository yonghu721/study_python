# python模块:一个.py文件就是一个模块,模块是python程序的基本组织单位.在模块中可以定义变量,函数,类,以及可执行的代码
# import 模块名
# import 模块名 as 别名
# from 模块名 import 功能名
# from 模块名 import 功能名 as 别名
# from 模块名 import *

#调用方式: ----> 模块名.功能名 / 别名.功能名
import random,os
random.randint(10,100)
for i in range(10):
    print(random.randint(10,100))

import random as rd
rd.randint(10,100)
#1. 导入模块中的功能  调用方式 ---> 功能名
from random import randint,choice
randint(10,100)

for i in range(10):
    print(randint(100,1000))

from random import randint as rint
rint(10,100)

from random import *
print(randint(10,100))











