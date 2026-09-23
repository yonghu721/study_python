# 1. 合并两个列表中的元素,并对合并的结果进行去重处理(出去列表中的重复元素)
#
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
# for num in num_list2:
#     num_list1.append(num)
# print(num_list1)
# new_list = []
# num_list1.sort()
# print(num_list1)
#
# for num in num_list1:
#     if num not in new_list:     #in判断元素是否存在于列表中,如果存在,则返回True;不存在,返回False
#         new_list.append(num)
# print(new_list)

num_list1 = [19,23,54,64,875,20,109,232,123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]
#解包:将列表这个一类容器解开成一个一个独立的元素
#组包:将多个值合并到一个容器
num_list = [*num_list1,*num_list2]
# for num in num_list2:
#     num_list1.append(num)


print(num_list)
new_list = []
num_list.sort()
print(num_list)

for num in num_list:
    if num not in new_list:     #in判断元素是否存在于列表中,如果存在,则返回True;不存在,返回False
        new_list.append(num)
print(new_list)

print("100是否存在num_list列表中(True为存在,False为不存在)",100 in num_list)  #not取反可以用于in中 例如 not in