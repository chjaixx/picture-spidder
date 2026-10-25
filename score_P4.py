#使用该学生成绩函数时需要传入一个学生姓名：成绩的字典
def add(students):
    try:
        print("请输入要增加的学生名字和成绩(两元素用空格隔开):")
        z = input().split()
        z_in = int(z[1])
        students[z[0]] = z_in
        print(f'学生{z[0]}增加成功')
    except Exception as f:
        print(f'请按提示输入正确的元素{f}')
def query(students):
    print("请输入要查看的学生名字(输入all查看全部):")
    n=input()
    if n in students:
        print(students[n])
    elif n=="all":
        print(students)
    else:
        print(f"学生{n}不存在")
def delect(students):
    print("请输入要删掉的学生姓名：")
    s = input()
    j = students.keys()
    if s in j:
        ss = students.pop(s)
        print(f"学生{ss}成功删除！")
    else:
        print("没有该学生")
#冒泡排序升序函数
def maopao(list_s):
    n=len(list_s)
    for i in range(n):
        for j in range(0,n-1-i):
            if list_s[j]>=list_s[j+1]:
                list_s[j],list_s[j+1]=list_s[j+1],list_s[j]
    return list_s
def args(*args):
    return args
def kwargs(**kwargs):
    return kwargs
#异常处理函数
def Except():
    try:
        print("测试输入：")
        nn=input()
        n=int(nn)
        a=n/0
    except Exception as f:
        print(f'异常{f}')