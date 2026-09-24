#--------------------------------------案例--------------------------------------------------------
"""
采用面向对象的编程思量,完成教务管理系统的开发.教务管理系统可以管理在校学生的成绩信息,通过控制台菜单与用户交互,具体的功能如下:
1. 添加学生成绩:根据输入的学生姓名,语文成绩,数学成绩,英语成绩,记录在系统中
2. 修改学生成绩:根据输入的学生姓名,修改对应的学生成绩
3. 删除学生成绩:根据输入的学生姓名,删除对应的学生成绩
4. 查询指定学生成绩:根据输入的学生姓名,查找对应的学生成绩,并输入
4.展示全部学生成绩:展示出系统中所有学生的成绩
"""

class Student:
    def __init__(self,name,chin,math,eng):
        self.name = name
        self.chin = chin
        self.math = math
        self.eng = eng
        print("Student 类型的对象初始化完毕,对象属性已填加完毕 .")

    def __str__(self):
        return f"姓名:{self.name} | 语文:{self.chin} | 数学:{self.math} | 英语:{self.eng} | 总分:{self.chin+self.math+self.eng}"

    def update_score(self,chin = None,math = None,eng = None):
        if chin is not None:
            self.chin = chin
        if math is not None:
            self.math = math
        if eng is not None:
            self.eng = eng

#教务管理系统
class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []
    #添加学生成绩
    def add_student(self):
        name = input("请输入学生姓名:")

        for i in self.student_list:
            if i.name == name:
                print("该学生已经存在,不需要进行添加!")
                return

        chin = int(input("请输入语文成绩:"))
        math = int(input("请输入数学成绩:"))
        eng = int(input("请输入英语成绩:"))

        if 0 <= chin <=100 and 0 <= math <= 100 and 0 <= eng <= 100:
            stu = Student(name, chin, math, eng)
            self.student_list.append(stu)
            print("学生信息添加成功~")
        else:
            print("学生的成绩应该在0-100之间,请重新输入!!")

    #修改学生成绩
    def update_student(self):
        name = input("请输入需要修改的学生姓名:")

        for i in self.student_list:
            if i.name == name:
                print(f"当前成绩为:{i}")

                chin = int(input("请输入语文成绩:"))
                math = int(input("请输入数学成绩:"))
                eng = int(input("请输入英语成绩:"))

                if 0 <= chin <= 100 and 0 <= math <= 100 and 0 <= eng <= 100:
                    i.update_score(chin,math,eng)
                    print("修改成功~")
                    print(f"修改后的成绩为:{i}")
                    return
                else:
                    print("各科成绩必须得在0-100之间!")
                    return

        print("没有找到该学生,无法修改")

    #删除学生成绩
    def delete_student(self):
        name = input("请输入需要删除的学生姓名:")

        for i in self.student_list:
            if i.name == name:
                self.student_list.remove(i)
                print("学生信息删除成功~")
                return

        print("未找到该学生,删除失败!")

    #查询指定学生成绩
    def query_student(self):
        name = input("请输入需要查询的学生姓名:")

        for i in self.student_list:
            if i.name == name:
                print(f"学生信息为:{i}")
                return

        print("未找到该学生,查询失败!")

    #展示全部学生成绩
    def all_student(self):
        for i in self.student_list:
            print(i)

    #运行系统
    def run(self):
        print(f"欢迎使用{EduManagement.system_name}!当前版本为:V{EduManagement.system_version}")
        print()
        while True:
            print()
            print("========================================================================")
            print("1.添加学生   2.修改学生   3.删除学生   4.查询指定学生   5.查询所有学生   6.退出系统")
            print("========================================================================")

            choice = int(input("请选择要执行的操作,输入1-6:"))

            match choice:
                case 1:
                    self.add_student()
                case 2:
                    self.updata_student()
                case 3:
                    self.delete_student()
                case 4:
                    self.query_student()
                case 5:
                    self.all_student()
                case 6:
                    print("Bye ~ Bye ~")
                    break
                case _:
                    print("输入错误,请选择1-6之间的菜单功能")



if __name__ == '__main__':
    EduManagement().run()