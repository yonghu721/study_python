#set 集合 : set会自动去重,存储不重复的元素
#集合是一种无序的,不可重复的,可修改的数据容器
#定义
# s1 = {1,2,3,4,5,123,12,3,1,23,4,12,32,12,3,2,1,4,23,6}
# s2 = set()
# print(type(s1),type(s2))
# print(s1)

#常见操作
# 添加:s1.add()
# 删除:s1.remove()/s1.pop()/s1.clear()
# 交/并/差集:s1.intersection(s2)/s1.union(s2)/s1.difference(s2)

#案例:根据提供的班级学生的选课情况,完成如下需求:
'''
      1. 找出同时选修了法语和艺术的学生
      2. 找出同时选修了所有四门课程的学生
      3. 找出选修了足球,但是没有选修篮球的学生
      4. 统计每一个学生选修的课程数量
'''
#选修足球学生名单
football_set = {"王林","增牛","徐立国","遁天","天运子","韩立","厉飞雨","乌丑","紫灵"}
#选修篮球学生名单
basketball_set = {"张铁","墨居仁","王林","姜老道","曾牛","王婵","韩立","天运子","李化元","厉飞雨","云露"}
#选修法语学生名单
french_set = {"许木","王卓","十三","虎咆","姜老道","天运子","红蝶","厉飞雨","韩立","曾牛"}
#选修艺术学生名单
art_set = {"遁天","天运子","韩立","虎咆","姜老道","紫灵"}

#1. 找出同时选修了法语和艺术的学生
#方式一.
print(french_set.intersection(art_set))
#方式二: & --> 交集
print(french_set & art_set)

#2. 找出同时选修了所有四门课程的学生
a1 = football_set & basketball_set & french_set & art_set
print(a1)

#3. 找出选修了足球,但是没有选修篮球的学生
print(football_set .difference(basketball_set))
#方式二: - --->  差集 在a中有但是在b中没有
fb_set2 = football_set - basketball_set
print(fb_set2)

#方式三: 集合推导式 ---> 快速构建集合,语法:{要忘集合中添加的数据 for s in set1 if 条件}
fb_set3 = {s for s in football_set if s not in basketball_set}
print(fb_set3)

#4. 统计每一个学生选修的课程数量
#4.1 获取到学生的名单也就是并集
#方式一:
# all_set1 = football_set.union(basketball_set).union(french_set).union(art_set)
# print(all_set1)
#方式二:  并集 (|)
all_set = football_set | basketball_set | french_set | art_set
print(all_set)

all_list = [*football_set,*basketball_set,*french_set,*art_set]

for i in all_set:
    print(f"同学:{i}选修了{all_list.count(i)}门课程")

#集合set操作的运算符:  & 交集  | 并集   - 差集
#集合推导式的写法:
#   变量名称 = {i表达式 for i in 列表}
#   变量名称 = {i表达式 for i in 列表 if 条件}









