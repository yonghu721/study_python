# #1.打开文件
# f = open("resources/测试文件","r",encoding="utf-8")
# #2.读取文件
# #read 读取全部内容
# #readline 一行一行的读取
# #readlines 读取全部内容并返回一个列表
#
# # content = f.read()
# # print(content)
#
# content_list = f.readlines()
# for i in content_list:
#     print(i.strip())
#
# #3.关闭文件
# f.close()


# #1.打开文件
# f = open("resources/测试文件2-静夜思.txt","w",encoding="utf-8")
# #2.写入文件
# f.write("静夜思(李白)\n\n")
#
# f.write("窗前明月光,\n")
# f.write("疑是地上霜。\n")
# f.write("举头望明月,\n")
# f.write("低头思故乡。")
#
# #3.关闭文件
# f.close()

#---------------------------------文件操作-资源释放 - 方式一----------------------------------------------
# #1.打开文件
# f = open("resources/测试文件2-静夜思.txt","w",encoding="utf-8")
# #2.写入文件
# try:
#     f.write("静夜思(李白)\n\n")
#     f.write("窗前明月光,\n")
#     f.write("疑是地上霜。\n")
#     f.write("举头望明月,\n")
#     f.write("低头思故乡。")
#
# finally:
#     #3.关闭文件
#     f.close()
#     print("关闭文件")

#=========================================释放资源 -方式二===========================================
#释放资源--推荐方式
#with语句(上下文管理器)的核心作用就是确保资源的总是被正确获取和释放(即使发生异常,也会被正确释放),也是项目开发中的推荐方式
# with open("resources/测试文件2-静夜思.txt","w",encoding="utf-8") as f:
#     f.write("静夜思(李白)\n\n")
#     f.write("窗前明月光,\n")
#     f.write("疑是地上霜。\n")
#     f.write("举头望明月,\n")
#     f.write("低头思故乡。")

#====================================读写json格式文件=======================================================
#写入json数据文件
"""
    dump() :将python对象序列化为json格式字符串并写入文件
    load() :从文件中读取json格式数据,并将其反序列化为python对象
"""
import json
user = {
    "name":"涛哥",
    "age":18,
    "gender":"男",
    "hobbies":["coding","reading","traveling"]
}
with open("resources/user.json","w",encoding="utf-8") as f:
    #ensure_ascii:默认为True,确保所有的数据输出的数据都是ASCII编码,
    # 设置为False,则输出的数据为中文,非ASCII码为原样输出
    #indent:会在输出的jso数据中添加缩进
    json.dump(user,f,ensure_ascii=False,indent = 4)

#读取json数据文件
with open("resources/user.json","r",encoding="utf-8") as f:
        user = json.load(f)
        print(user)
        print(type(user))




