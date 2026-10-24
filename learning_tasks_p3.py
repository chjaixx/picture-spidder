s='python adwfa python chj dasdas chj dsada chj puthon adsad python chj'
dict_s={}
list_s=s.split()
# num_py=0
# num_chj=0
# for i in list_s:
#     if i=='python':
#         num_py+=1
#     else:
#         if i=='chj':
#             num_chj+=1
# dict_s['python']=num_py
# dict_s['chj']=num_chj

#dict统计一段文本中单词出现的次数
for i in list_s:
    if i in dict_s:
        dict_s[i]+=1
    else:
        dict_s[i]=1
print(dict_s)
#set对列表去重
set_li=set(list_s)
list_s=list(set_li)
print(list_s)
#实现学生成绩的增删改查
students={'梨花':78,'李华':88,'王伟':88}
q=True
while q:
    print("请输入对应序号表示需要实现的业务：实现学生成绩的1.增2.删3.改4.查5.退出:")
    n=int(input())
    if n==1:
        print("请输入要增加的学生名字和成绩(两元素用空格隔开):")
        z=input().split()
        z_in=int(z[1])
        students[z[0]]=z_in
        print(f'学生{z[0]}增加成功')
        continue
    if n==2:
        print("请输入要删掉的学生姓名：")
        s=input()
        j=students.keys()
        if s in j:
            ss=students.pop(s)
            print(f"学生{ss}成功删除！")
        else:
            print("没有该学生")
        continue
    if n==4:
        print(students)
        continue
    if n==3:
        print("请输入要修改的学生名字和成绩(两元素用空格隔开):")
        x=input().split()
        x_int=int(x[1])
        jj = students.keys()
        if x[0] in jj:
            students[x[0]]=x_int
            print(f"学生{x[0]}成功修改！")
        else:
            print("没有该学生")
        continue
    if n==5:
        q=False
        print('成功退出！')
    else:
        print("请按提示正确输入：")

# add=students.append({'张三':67})
# del_stu=students.pop(students[2])
# delter=students
# cc=students[]
#找出两列表的交集与并集
s1='chj pychon python chj chj python sdadf'
s2=s1.split()
s2_set=set(s2)
s_set=set(list_s)
s3=s2_set|s_set
s2=list(s3)
s4=s2_set&s_set
s4=list(s4)
print(f"list_s与s2表的并集为{s3}交集为{s4}")
#反转列表，找出列表最大值与最小值（不调用内置函数各实现一次）
su=[1,2,3,55,67,8,3]
li=reversed(su)
max_su=su[0]
min_su=su[0]
sue=list(li)
print(f"函数实现反转列表{sue}列表最大值{max(su)}与最小值{min(su)}")
for i in su:
    if i>max_su:
        max_su=i
    elif i<min_su:
        min_su=i
print(f"反转列表{su[::-1]}列表最大值{max_su}与最小值{min_su}")
