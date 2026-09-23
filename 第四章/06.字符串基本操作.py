# #字符串 基本操作 --> 字符串是无法修改的,有序性,可迭代性
#
# s = "   hello-world-Hello-Word   "
# #find() 查找指定字符串第一次出现的索引位置
# index = s.find("-")
# print(index)
#
# #count() 统计子字符串在指定字符串中出现的次数
# c = s.count("o")
# print(c)
#
# #upper() 转为大写
# a = s.upper()
# print(a)
#
# #lower() 转为小写
# s2 = s.lower()
# print(s2)
#
# #split() 将字符串按早指定字符串切割 - 列表
# slist = s.split("-")
# print(slist)
#
# #strip() 去除字符串两端的空格
# ss = s.strip()
# print(ss)
#
# #replace() 将字符串中的指定子串替换为新的内容
# sr = s.replace(" ", "-")
# print(sr)
#
# #startswith /endswith() 判定字符串是否以制定的字符串开始/结尾 , 返回布尔值
#
# print(s.startswith(" "))
# print(s.endswith(" "))

#案例
#1. 邮箱格式验证:用户输入一个邮箱,验证邮箱格式是否正确(包含一个@和至少一个.),如果输入正确,输出"邮箱格式正确",否则输出"邮箱格式错误"


# while True:
#     username = input("请输入邮箱:")
#     if username.count("@") == 1 and username.count(".") >= 1:
#         print("邮箱格式正确")
#         break
#     else:
#         print("邮箱格式错误,请重新输入!!!")

#方式二: in 运算符 --> 判断子串是否存在字符串中,存在,返回True;否则,返回False

# while True:
#     username = input("请输入邮箱:")
#     if username.count("@") == 1 and "." in username:
#         print("邮箱格式正确")
#         break
#     else:
#         print("邮箱格式错误,请重新输入!!!")

# huiwen = input("请输入一段字符串:")
# if huiwen == huiwen[::-1]:
#     print("是回文!")
# else:
#     print("不是回文!")

new_list = []
for i in range(10):
    num = input(f"请输入第{i+1}个字符串")
    new_list.append(num)
    new_list.reverse()

for j in new_list:
    print(j.upper())


print(new_list)