"""
特性           字符串         列表          元组          集合          字典
有序性          有序          有序          有序          无序          有序
重复元素        允许          允许          允许         不允许          key不允许
可变性         不可变         可变          不可变         可变          可变
索引访问        支持          支持          支持          不支持         不支持
切片操作        支持          支持          支持          不支持         不支持
使用场景       文本处理    有序可重复数据集合  固定数据记录    去冲个数据集合   键值对

"""

print("欢迎使用教务管理系统!")
# {张三:{语文:89,数学:88,英语:99}}
studen_app = {}
stu = """
=============教务管理系统=================
            1.添加学生信息
            2.修改学生信息
            3.删除学生信息
            4.查询学生信息
            5.列出所有学生
            6.统计班级成绩
            7.退出系统
========================================
"""


while True:
    print(stu)
    choice = input("请选择需要执行的操作(1-7):")

    match choice:
        case "1":
            name = input("请输入学生的姓名:")

            if name in studen_app:
                print(f"{name}同学的成绩信息已存在,请重新选择!")
            else:
                chinese = int(input("请输入学生的语文成绩:"))
                math = int(input("请输入学生的数学成绩:"))
                eng = int(input("请输入学生的英语成绩:"))
                studen_app[name] = {"语文":chinese,"数学":math,"英语":eng}
                print(studen_app)
                print(f"{name}同学以录入成功!")

        case "2":
            name = input("请输入需要修改的同学姓名:")
            if name not in studen_app:
                print(f"{name}同学不存在,请重新输入")
            else:
                chinese = int(input("请输入学生学修改后的语文成绩:"))
                math = int(input("请输入学生修改后的数学成绩:"))
                eng = int(input("请输入学生修改后的英语成绩:"))
                studen_app[name] ={"语文":chinese,"数学":math,"英语":eng}
                print(studen_app)
                print(f"{name}同学的成绩修改成功!")

        case "3":
            name = input("请输入需要删除的同学姓名:")
            if name not in studen_app:
                print(f"{name}同学不存在,请重新选择!")
            else:
                del studen_app[name]
                print("删除成功!")

        case "4":
            name = input("请输入需要查询的同学姓名:")
            if name not in studen_app:
                print("该同学不存在,请重新输入!")
            else:
                for i in studen_app.keys():
                    info = studen_app[name]
                print(f"姓名:{name},语文:{info["语文"]},数学:{info["数学"]},英语:{info["英语"]}")

        case "5":
            for name in studen_app.keys():
                info = studen_app[name]
                print(f"姓名:{name},语文:{info["语文"]},数学:{info["数学"]},英语:{info["英语"]}")
        case "6":
            if not studen_app:
                print("暂无该学生数据,无法统计!")
            else:

                chinese_list = []
                math_list = []
                eng_list = []
                for name,score_dict in studen_app.items():
                    chinese_list.append((score_dict["语文"],name))
                    math_list.append((score_dict["数学"],name))
                    eng_list.append((score_dict["英语"],name))

                # 语文统计
                ch_max, ch_max_name = max(chinese_list)
                ch_min, ch_min_name = min(chinese_list)
                ch_avg = sum([x[0] for x in chinese_list]) / len(chinese_list)

                # 数学统计
                ma_max, ma_max_name = max(math_list)
                ma_min, ma_min_name = min(math_list)
                ma_avg = sum([x[0] for x in math_list]) / len(math_list)

                # 英语统计
                en_max, en_max_name = max(eng_list)
                en_min, en_min_name = min(eng_list)
                en_avg = sum([x[0] for x in eng_list]) / len(eng_list)

                print(f"语文最高分:{ch_max},最低分:{ch_min},平均分:{ch_avg:.2f}")
                print(f"数学最高分:{ma_max},最低分:{ma_min},平均分:{ma_avg:.2f}")
                print(f"英语最高分:{en_max},最低分:{en_min},平均分:{en_avg:.2f}")
                print(
                    f"语文最高分的学生姓名为{ch_max_name},数学最高分的学生姓名为:{ma_max_name},英语最高分的学生姓名为:{en_max_name}")
                print(
                    f"语文最低分的学生姓名为{ch_min_name},数学最低分的学生姓名为:{ma_min_name},英语最低分的学生姓名为:{en_min_name}")

        case "7":
            print("欢迎下次使用,再见!!!")
            break
        case _:
            print("输入错误,请输入有效的操作!!!")