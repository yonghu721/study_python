# from types import NoneType
#
# print('hello')
# print(type('hello'))
# a = 100
# print(type(a),type('hello'))
# print(type(None))
# print(type(False))
# print(type(3.1415926))
# print(type('nihao'))
# #通过isinstance()判定数据是否属于指定的类型,返回的是一个bool值,
# # 具体语法为:isinstance(数据,类型)
# print(isinstance(5,int))
# print(isinstance(True,int))
# print(isinstance(True,bool))
# print(isinstance(1.31,int))
# print(isinstance(False,bool))
# print(isinstance(a,int))
# print(isinstance("abcd",int))
# print(isinstance(1111,NoneType))

# 如何查看数据的实际类型
# type()
# isinstance()

# s3 = """
# 我要学习python
#         我要月入13000
# """
# print(s3)
#
# s2 = "It's very interesting"
# print(s2)
#
# s3 = 'It\'s very interesting'
# print(s3)
#转义字符\
#\' 单引号  表示单引号'
# \" 双引号 表示双引号
# \n 换行符 开始新的一行 (换行)
# \t 制表符 增加缩进,锁紧一个制表符(tab) 的大小

# s4 = "It's\n very interesting"
# s5 = "It's\t very interesting"
# print(s4)
# print(s5)
# msg = "Hello 的意思是 \"你好\""
# msg2 = '\tHello 的意思是 \n\t"你好"'
# print(msg)
# print(msg2)

# 1. 字符串的定义方式
# 单引号,双引号,三引号
# 2. 常见的转义字符
# \' (单引号) \" (双引号) \n (换行) \t (制表符)
#3. 字符串的使用原则
# 单引号和双引号都是等效的,项目中保持一种写法即可
# 三引号:多行字符串等场景

# 4. 字符串的拼接
# 多个字符串字面量可以直接写或者用+号进行拼接

# smg = "黑马程序员" "学习python"
# print(smg)
#
# print("黑马程序员"+"学习python")
# s1 = "学习python"
# s2 = "月入过万"
# s3 = "人生苦短我用python"
# print("黑马程序员:\n"+s1 + "," + s2 + "\t"+"," + s3)
#
# name = "朱一航"
# age = 23
# major = "软件工程"
# hobby = "python,agent"
# print("\"大家好,我是" + name + "今年" + str(age) +"岁" ", 学习的专业是" + major + ", 爱好是"+hobby + "\"")
#srt(int)--->将int类型的数字转为字符串
#+号只能拼接字符串与字符串不能拼接字符串与非字符串,如果要拼接只能将非字符串转成字符串类型才可以
#可以使用str(数字)的方式进行转换类型
# 缺点: 拼接繁琐 , 破坏字符串的完整性 , 类型转换

#效率更高的方式:字符串格式化
#通过 % 占位符的形式完成字符串和变量的快速拼接.
# (其中 % 表示我要占位 , s 表示将变量转换为字符串放入占位的位置)

smg_1 = "朱一航"
smg_2 = 23
print("大家好,我是 %s ,现在 %s 岁,我正在学习python,将来月入过万" % (smg_1,smg_2))
#多个变量要使用括号以及逗号,前面有多少个占位符,后面就要有多少个变量或数据,前后数量需要一致
print("大家好,我是%s ,我正在学习python" %smg_1)
# 字符串格式化 方式一: %s 占位符
name = "朱一航"
age = 23
major = "软件工程"
hobby = "python,agent"
print("大家好,我是%s,今年%s岁,学习的专业是%s,爱好是%s" % (name,age,major,hobby))

# 字符串格式化 方式二: f"内容{变量/表达式}" ----->  推荐方式
#直接在前面+f然后使用{}把变量或者表达式{}起来
print(f"大家好,我是{name},今年{age}岁,学习的专业是{major},爱好是{hobby}")

