#while 循环
#while 条件表达式:
    # 循环体语句1
    # 循环体语句2
    #
# i=0
# while i<10:
#     i += 1
#     print(f"人生苦短,我用python:{i}")
#
# else:
#     print("循环正常结束,执行完毕")

#计算1-100之间所有偶数的累加之和
# i=1
# count=0
# while i<=100:
#     if(i%2==0):
#         count+=i
#         print(f"{i}是偶数计入累加")
#     i+=1
# else:
#     print(f"循环正常结束1-100之间所有的偶数累加之和为:{count}")

#for循环
#while循环是通过条件表达式来控制是否要进行下一次循环的.而for循环,本质是一种轮训遍历机制,对一批内容进行逐个处理.
#for循环结构
# for 元素 in 待处理数据集:
#     循环体代码(对元素进行处理)
# else:
#     循环结束时,执行的代码

# msg = "hello-python!"
# for i in msg:
#     print(i)
# else:
#     print("循环结束")

# range 语句
# 作用:生成指定规则的数字序列
# 用法1:range(end) -> 获取一个从0开始,到end结束的数字序列(不含end本省)
#     range(5) 获取的数据就是0,1,2,3,4
# 用法2:range(start,end) -> 获取一个从start开始,到end结束的数字序列(不含end本身)
#     range(2,8)获取的数据就是2,3,4,5,6,7
# 用法3:range(start,end,step) -> 获取一个从start开始,到end结束的数字序列,step步长(不含end本身)
#     range(0,10,2)获取的数据就是0,2,4,6,8

#计算1-100之间所有奇数的和
# count = 0
# for i in range(1,101,2):
#     count+=i
#     print(i)
# print(f"1-100之间所有的奇数的和为:{count}")

#计算100-500之间所有3的倍数的数字之和
# count = 0
# for i in range(100,501):
#     if i % 3 ==0:
#         count+=i
#         print(i)
# print(count)

#1. range(..)语句的作用是什么?
    # 生成指定规则的数字序列
    # 用法:
    # range(end)
    # range(start,end)
    # range(start,end,step)