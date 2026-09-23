# 2026年9月19日22-33级以学完
#需求: 根据输入的用户密码执行登录操作,具体要求如下:
# 1. 正确的用户名为admin/666888、zhangsan/123456、taoge/888666
# 2. 输入用户名和密码进行登录,知道登录成功,新恒旭结束运行;如果登录失败,则继续输入用户名和密码进行登录
# 3. 输入的用户名和密码不能为空!
# 4. 登陆成功:输出"登陆成功,进入B站首页"
# 5. 登录失败:输入"用户名或密码错误,请重新输入!"

#关键字
    # break: 只能够出现在循环汇总,表示结束/跳出循环的含义
    # continue:只能够出现在循环中,表示中断本次循环,直接进入下一次循环

# while True:  #while True 会一直循环,所以后面要使用关键字break,只能用在循环当中,用作跳出循环的操作
#     name = input("请输入账号:")
#     password = input("请输入密码:")
#     if name == "" or password == "":
#         print("用户名和密码不能为空!请重新输入")
#         continue  #continue 跳出本次循环
#     if (name == "admin" and password =="666888") or (name =="zhangsan" and password =="123456") or (name == "taoge" and password =="888666"):
#         print("登录成功,进入B站首页")
#         break
#     else:
#         print("用户名或密码错误,请重新输入!")
count=0
while True:
    username = input("请输入用户名:")
    password = input("请输入密码:")
    count+=1
    if (username == "admin" and password =="666888") or (username =="zhangsan" and password =="123456") or (username == "taoge" and password =="888666"):
        print("登录成功!")
        break
    elif count == 5:
        print("账号或密码输入错误5次,请稍后再试!!!")
        break
    else:
        print("账号或密码错误请重新输入")

