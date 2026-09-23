#1.定义一个函数:根据传入的底和高计算三角形面积的函数(三角形面积 = 底 * 高 / 2)
# def triangle_area(x,y):
#     """
#     根据传入的底和高计算三角形面积
#     :param x: 底长
#     :param y: 高
#     :return: 三角形面积
#     """
#     area=x*y/2
#     return area
# print(f"三角形面积为:{triangle_area(3,4)}")
#
# #2.
# def count_vowel(s):
#     """
#     统计元音字母的个数
#     :param s: 传入的字符串
#     :return: 统计的元音字母的个数
#     """
#     num = 0
#     for i in s:
#         if i in "aeiouAEIOU":
#             num+=1
#     return num
# print("元音字母的个数为:",count_vowel("hello word"))
#
# #3.
# def calc_score(score_list):
#     """
#     计算传入的班级学院高考成绩列表中趁机的最高分,最低分,平均分
#     :param score_list:分数列表
#     :return:最高分,最低分,平均分
#     """
#     max_s = max(score_list)
#     min_s = min(score_list)
#     avg_s = round(sum(score_list)/len(score_list),1)
#     return max_s,min_s,avg_s
#
# s_list = [50,60,55,65,78,56,989,45,56,8,454,565,78]
# max_score,min_score,avg_score = calc_score(s_list)
# print("最高分:",max_score)
# print("最底分:",min_score)
# print("平均分:",avg_score)


#4.
# def Fraction(n):
#     """
#     根据传入的分数,计算对应的分数等级并返回
#     :param n: 分数
#     :return: 分数对应的等级
#     """
#     if n>=90:
#         return "A"
#     elif n>=75:
#         return "B"
#     elif n>=60:
#         return "C"
#     else:
#         return "D"
#
# print(Fraction(80))

#5.
def palindrome(s):
    """
    判断一个字符串是否是回文串
    :param s:字符串
    :return:bool值True或者False
    """
    return s == s[::-1]

print(palindrome("abcdefed"))
print(palindrome("abcdcba"))

#6.
def time(seconds):
    """
    将传入的秒转换为小时,分钟,秒
    :param seconds:秒
    :return:小时,分钟,秒
    """
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return h, m, s
print(time(69940))

#7.
def triangle(a,b,c):
    """
    判断三角形的类型(等边,等腰,普通,或者不能构成三角形)
    :param a: 第一条边
    :param b: 第二条边
    :param c: 第三条边
    :return:
    """
    if a+b>c and a+c>b and b+c>a:
        print("可以构建三角形")
        if a==b==c:
            print("等边三角形")
        elif a==b or b==c or c==a:
            print("等腰三角形")
        else:
            print("普通三角形")
    else:
        print("不能构建三角形")

triangle(20,20,30)
