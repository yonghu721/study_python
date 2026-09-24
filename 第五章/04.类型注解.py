#----------------------------类型注解---------------------------------------
# 类型注解是python中的一种语法特写,用于明确标识变量,函数参数和返回值的数据类型,从而使代码更清晰,更安全,更易于维护
#变量定义 - 未指定类型注解  ---> 类型推断
a = 595
score = 98.5
hobby = "Python"
flag = True
pic = None

name = ["A","B","C"]
phones = {"13476543254","123456789321","18888888821"}
options = {"count":2,"total":10}
goods = ("手机",6999,1)

#变量定义 - 指定类型注解
a1 : int= 595
score1 : float = 98.5
hobby1 : str= "Python"
flag1 : bool= True
pic1 : None = None

name1 :list[str | int | float] = ["A","B","C"]
phones1 :set[str] = {"13476543254","123456789321","18888888821"}
options1 : dict[str,int] = {"count":2,"total":10}
goods1 : tuple[str,int,int] = ("手机",6999,1)

name1.append("A")
name1.append(100)
name1.append(198.5)

print(name1)

#----------------------------------------函数的类型注解----------------------------------------
#为函数添加类型注解,其实主要就是为函数的参数和返回值添加类型注解,其具体语法如下:
#函数类型注解
def aircle_area_len(r:float) -> tuple[float ,float ]:
    return round(3.14 * r * r,1),round(2 * 3.14 * r,1)

al = aircle_area_len(3.1)
print(al)














