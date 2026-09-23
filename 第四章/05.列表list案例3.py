# # 1. 生成1-20 的平方列表
# num_list1 = []
# for i in range(1,21):
#     num_list1.append(i ** 2)
# print(num_list1)
#
# #列表推导式 --> 就是按照一定的规则快速生成一个列表的方法 --> 语法格式:[要插入的值 for i in 序列/列表]
# num_list2 = [i**2 for i in range(1,21)]
# print(num_list2)

# # 2. 从如下数字列表中提取所有偶数,并计算其平方,组成一个新的列表
# new_list = []
# num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]
# for num in num_list:
#     if num % 2 ==0:
#         print(num)
#         new_list.append(num ** 2)
# # new_list.sort()
# print(new_list)
# # 列表推导式语法格式2 --> [要插入的值 for i in 序列/列表 if 条件]
# new_list1 = [i ** 2 for i in num_list if i%2 == 0]
# print(new_list1)

# list1 = ['M','A','C','E','F','G','H','L','N','I','J','K','O']
# list2 = ['X','Z','Y','D','E','F','G']
# list3 = ['W','A','S','D']
# new_list = []
# new_list1 = list1+list2+list3
# new_list1.sort()
# print(new_list1)
# for i in new_list1:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

# list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# new_list = [i ** 2 for i in list1 if i%3 == 0 or i%5 == 0]
# print(new_list)

list1 = [11,2,31,4,-5,15,17,28,49,10,-11,16,54,-14,36,-16,87,-39]
new_list = [i for i in list1 if i>0]
print(new_list)

