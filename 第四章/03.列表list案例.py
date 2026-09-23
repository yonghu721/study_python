#1.将用户输入的10个数字,存储到一个列表中,并将列表中的数字进行排序,输出其中的最小值,最大值和 平均值.
s = []
for i in range(1,11):
    x = int(input(f"请输入第{i}个数字:"))
    s.append(x)

print(s)
s.sort()
print(f"最小的值为:{s[0]}")
print(f"最大的值为:{s[-1]}")
print(max(s))
print(min(s))
#sum()求和;len()获取元素的个数(列表的长度)length
#sum可以直接计算列表的和,len可以计算列表的长度
print(f"这个列表的平均值为:{sum(s)/len(s)}")
print(s)