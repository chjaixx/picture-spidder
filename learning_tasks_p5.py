class Student:
    def __init__(self,sid,name,age):
        self.sid=sid
        self.name=name
        self.age=age
    def Prin(self):
        return f"学号：{self.sid},姓名：{self.name},年龄：{self.age}"
class Student1(Student):
    def __init__(self,sid,name,age,allager):
        super().__init__(sid,name,age)
        self.allager=allager
    def Prin(self):
        return f"学号：{self.sid},姓名：{self.name},年龄：{self.age},总分：{self.allager}"
class StudentManager:
    def __init__(self,file_name='studentP5'):
        self.file_name=file_name
    def load_data(self):
        self.st_li = []
        try:
            with open(self.file_name,'r',encoding='utf-8') as f:
                for li in f.readlines():
                    li=li.strip()
                    if not li:
                        continue
                    sid,name,age,allager=li.split(",")
                    s=Student1(sid,name,int(age),int(allager))
                    self.st_li.append(s)
        except Exception as e:
            print('文件txt不存在',e)
    def stu_add(self,sid,name,age,allager):
        with open(self.file_name,'a',encoding='utf-8') as f:
            f.write(f"{sid},{name},{age},{allager}\n")
        self.load_data()
    def selectall(self):
        self.load_data()
        for stu in self.st_li:
            print(stu.Prin())
    def stu_del(self):
        self.load_data()
        sid_del = input("请输入要删除的学生学号：")
        exist = False
        new_list = []
        for stu in self.st_li:
            if stu.sid == sid_del:
                exist = True
            else:
                new_list.append(stu)
        if not exist:
            print("查无此人！")
            return
        with open(self.file_name, 'w', encoding='utf-8') as f:
            for stu in new_list:
                f.write(f"{stu.sid},{stu.name},{stu.age},{stu.allager}\n")
        self.load_data()
        print("删除成功！")
    def stu_update(self):
        self.load_data()
        sid_up = input("请输入要修改的学生学号：")
        allager_up=input("请输入要修改的学生分数：")
        exist = False
        new_list = []
        for stu in self.st_li:
            if stu.sid == sid_up:
                stu.allager=allager_up
                exist = True
            new_list.append(stu)

        if not exist:
            print("查无此人！")
            return
        with open(self.file_name, 'w', encoding='utf-8') as f:
            for stu in new_list:
                f.write(f"{stu.sid},{stu.name},{stu.age},{stu.allager}\n")
        self.load_data()
        print("修改成功！")

    def stu_find(self):
        self.load_data()
        sid_find = input("请输入要查询的学生学号：")
        exist = False
        for stu in self.st_li:
            if stu.sid == sid_find:
                print(stu.Prin())
                exist = True
                break  # 找到就直接跳出循环，不用继续往下找
        if not exist:
            print("查无此人！")

    def count_line(self):
        try:
            with open(self.file_name, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                real_lines = [line for line in lines if line.strip()]
                return len(real_lines)
        except Exception as e:
            print("读取失败：", e)
def main():
    manager = StudentManager('studentP5')
    while True:
        print("-----学生管理系统-----")
        print("1.添加学生")
        print("2.查询全部学生")
        print("3.删除学生（按学号）")
        print("4.修改学生分数（按学号）")
        print("5.查询单个学生（按学号）")
        print("6.查看学生总人数")
        print("0. 退出系统")
        choice = input("请输入你的选择：")
        if choice == "1":
            sid = input("输入学号：")
            name = input("输入姓名：")
            age = input("输入年龄：")
            allager = input("输入总分：")
            manager.stu_add(sid, name, age, allager)
        elif choice == "2":
            manager.selectall()
        elif choice == "3":
            manager.stu_del()
        elif choice == "4":
            manager.stu_update()
        elif choice == "5":
            manager.stu_find()
        elif choice =="6":
            print(f'总人数：{manager.count_line()}人')
        elif choice == "0":
            print("程序退出")
            break
        else:
            print("输入错误，请输入0~4之间的数字！")
if __name__ == '__main__':
    main()
    # n=StudentManager('studentP5')
    # #n.stu_add('003','梨花',18,450)
    # n.selectall()
    # #n.stu_del()
    # # print(n.st_li)
    # n.stu_update()


