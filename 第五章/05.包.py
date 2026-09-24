#包:本质就是一个文件夹,该文件夹中可以包含若干python模块(.py文件),文件夹下还包含了一个__init__.py
#作用:模块文件较多时,用来管理多个模块.(包的本质就是一个模块)
# import 包名.模块名
# from 包名 import 模块名
# from 包名 import *
# from 包名.模块名 import 功能名
# from 包名.模块名 import *

#1. 导入模块
import utils.my_fun
utils.my_fun.log_separator1()
utils.my_fun.log_separator2()
utils.my_fun.log_separator3()

from utils.my_fun import log_separator4
log_separator4()

#如果要通过from utils import * 导入包下的所有模块,需要在__init__.py 文件中添加 __all__ = []

from utils import *
my_fun.log_separator4()
print(my_var.NAME)
print(my_fun.PI)

#2. 导入模块中的功能
from utils.my_var import NAME,PI
print(NAME)
print(PI)