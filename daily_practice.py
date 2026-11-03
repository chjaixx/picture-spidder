# num=0
# c=0
# for i in range(1,2020):
#     ls =list(str(i))
#     g =['1','2','0','9']
#     for j in ls:
#         if j in g:
#             num+=1
#             c+=i*i
#             break
# print(f'平方和为{c},个数为{num}')
# nambers=[1,2,3,4,5]
# squ=list(map(lambda x:x**2,nambers))
# print(squ)
# num=int(input('请输入一个数：'))
# for i in range(2,num):
#     if num%i==0:
#         print('不是素数')
#         break
# else:
#     print('是素数')
#1-100偶数的平均值
# num=0
# li=0
# for i in range(1,101):
#     if i%2==0:
#         num+=i
#         li+=1
# print(num,li,num/li)

# class Circle:
#     def __init__(self,r=0):
#         self.__radius=r
#     def __del__(self):
#         print(f'半径为{self.__radius}被删除')
#     def SetRahf(self,rr):
#         self.__radius=rr
#     def Area(self):
#         return 3.14*self.__radius**2
#     def __str__(self):
#         return f'半径为{self.__radius}的面积为{self.Area()}'
#     def __gt__(self, other):
#         return self.Area()>other.Area()
# t=Circle()
# t1=Circle(2)
# t.SetRahf(3)
# print(t,t1)
# print(t>t1)

# nuu=0
# for i in range(1,11):
#     cj=1
#     for j in range(1,i+1):
#         cj*=j
#     nuu+=cj
# print(nuu)
#
# def lj(x):
#     if x==1:
#         return 1
#     return x*lj(x-1)
# s=0
# for i in range(1,11):
#     s+=lj(i)
# print(s)

# s1=0
# s2=0
# for i in range(1,41):
#     for j in '2019':
#         if j in str(i):
#             s1+=i**2
#             s2+=1
#             break
# print(s1,s2)
# s3,s4=0,0
# for i in range(1,2020):
#     if '2' in str(i) or'0' in str(i) or'1' in str(i)or'9' in str(i):
#         s3+=i**2
#         s4+=1
# print(s3,s4)
#时间格式
# class Mtime:
#     def __init__(self,hour=0,min=0,sec=0):
#         self.hour=hour
#         self.min=min
#         self.sec=sec
#     def get_time(self):
#         return f'{self.hour}:{self.min}:{self.sec}'
#     def set_time(self,hour1,min1,sec1):
#         self.hour = hour1
#         self.min = min1
#         self.sec = sec1
#         return f'{self.hour}:{self.min}:{self.sec}'
# t=Mtime(16,34,22)
# print(t.get_time())
# print(t.set_time(12,34,60))
# f=10
# print(f"dsd{f-1}")
# q='q'
# num=0
# cont=0
# aug=0
# dd=input("输入任意数字，q结束：")
# while dd!=q:
#     nu = float(dd)
#     num += nu
#     cont+=1
#     aug = num / cont
#     dd=input("输入任意数字，q结束：")
# print(aug)

# t=1
# num=0
# while t<=100:
#     num+=t
#     t+=1
# print(num)

# import random
# nan=random.randint(1,100)
# i=1
# nann=True
# while nann:
#     na = input("输入一个数：")
#     na=int(na)
#     if na < nan:
#         print(f"第{i}次没有中")
#         print("小了")
#     elif na>nan:
#         print(f"第{i}次没有中")
#         print("大了")
#     else:
#         print(f"第{i}次猜中了")
#         nann = False
#     i += 1

# i=True
# a=input()
# c=0
# while i:
#     b=input()
#     a=int(a)
#     b=int(b)
#     c=a+b
#     i=False
# print(c)

# num=0
# n='ithaeiama'
# for i in n:
#     n='a'
#     if n==i:
#         num+=1
# print(num)
#

# for i in range(1,11):
#     for j in range(1,i+1):
#         print(f'{j}*{i}={j*i}\t',end='')
#     print('\n')

# money=8000
# for i in range(21):
#     import random
#     x=random.randint(1,10)
#     if x<5:
#         print(f"{i}没达标")
#         continue
#     if x>=5 and money>=1000:
#         money-=1000
#         print(f'{i}发工资1000公司还剩{money}')
#         continue
#     else:
#         print(f"{i}公司没钱了")
#         break

# agelist=[21,25,21,22,23,20]
# agelist.append(31)
# print(agelist)
# agenew=[29,33,30]
# agelist.extend(agenew)
# print(agelist)
# qu_1=agelist.pop(0)
# qu_2=agelist.pop(-1)
# print('取出',qu_1,qu_2)
# print('31下标',agelist.index(31))

# ttlist=[1,2,3,4,5,6,7,8,9,10]
# def ttfor():
#     newlis=[]
#     for i in ttlist:
#         if i%2==0:
#             newlis.append(i)
#     print(newlis)
# def ttwhile():
#     newlis=[]
#     i=0
#     while i<len(ttlist):
#         if ttlist[i]%2==0:
#             newlis.append(ttlist[i])
#         i+=1
#     print(newlis)
# if __name__ == '__main__':
#     ttfor()
#     ttwhile()

# strr='itheima ityuan comter'
# print(strr.count('it'))
# strr=strr.replace(' ','|')
# print(strr)
# print(strr.split('|'))

# pp="bca,gfey,jih"
# p=pp.split(',')
# print(p[1][2::-1])

# my_set={1,'a','b','c',5,6,67}
# print(my_set)

# add={
#     'wang':{
#         '部门':'科技部',
#         '工资':3000,
#         '级别':1
#     },
#     'zhou':{
#         '部门':'科技部',
#         '工资':5000,
#         '级别':2
#     },
#     'ling':{
#         '部门':'市场部',
#         '工资':7000,
#         '级别':3
#     },
#     'zhang':{
#         '部门':'科技部',
#         '工资':4000,
#         '级别':1
#     },
#     'liu':{
#         '部门':'市场部',
#         '工资':5000,
#         '级别':2
#     }
# }
# #得到员工名
# acs=add.keys()
# #对员工名进行遍历
# for acsh in acs:
#     #得到员工字典
#     ac=add[acsh]
#     #对符合条件的员工字典进行修改
#     if ac['级别']==1:
#         ac['级别']+=1
#         ac['工资']+=1000
# print(add)

# n=list(map(int,input().split('/n')))
# print(n)

# n=int(input())
# i=1
# while i<=n:
#     a=list(map(int,input().split()))
#     num=a[0]+a[1]
#     print(num)
#     i+=1
#素数的判断
# n=int(input())
# for i in range(1,n+1):
#     a=int(input())
#     if a<2:
#         print('No')
#         continue
#     for j in range(2,a):
#         if a%j==0:
#             print('No')
#             break
#     else:print('Yes')

#统计字符在文件中出现的次数
# with open('D:/测试.txt','r',encoding='utf-8') as f:
#     tt=f.read()
# t=tt.split()
# num=0
# for i in t:
#     if i=='chj':
#         num+=1
# print(t)
# print(f'chj出现的次数为：{num}')

#异常的传递性和处理
# def fanin1():
#     print('执行fanin1')
#     1/0
# def fanin2():
#     fanin1()
#     print('执行fanin2')
# def fanin3():
#     try:
#         fanin2()
#     except Exception as e:
#         print(f"有异常{e}")
#         print('执行fanxi3')
# if __name__ == '__main__':
#     fanin3()

#json数据转换
# import json
# s=[{'梨花':78},{'李华':88},{'张三':56},{'王伟':77}]
# s1=json.dumps(s,ensure_ascii=False)
# print(type(s1))
# print(s1)
# ss={'梨花':76,'李华':88,'张三':56,'王伟':77}
# s2=json.dumps(ss)
# print(type(s2))
# print(s2)
# s01='[{"梨花":78},{"李华":88},{"张三":56},{"王伟":77}]'
# s3=json.loads(s01)
# print(type(s3))
# print(s3)
# s02='{"梨花":76,"李华":88,"张三":56,"王伟":77}'
# s4=json.loads(s02)
# print(type(s4))
# print(s4)

#类和对象
# class student:
#     name=None
#     age=None
# stu1=student()
# stu1.name='梨花'
# stu1.age=19
# print(stu1.name,stu1.age)

# set1={1,2,3}
# set2={1,5,2,6}
# set3=set1.difference(set2)
# print(set3,set1,set2)
# set1.difference_update(set2)
# print(set1,set2)
# set4=set1.union(set2)
# print(set4)

#成员变量和成员方法
# class student:
#     name=None
#     def say_hi1(self):
#         print(f"大家好，我是{self.name},多多关照")
#     def say_hi2(self,mag):
#         print(f"大家好，我是{self.name},{mag}")
# s1=student()
# s1.name='梨花'
# s1.say_hi1()
# s2=student()
# s2.name="苏沫"
# s2.say_hi2("泡沫的沫")

#类和对象关系
# class clone:
#     id=None
#     jg=None
#     def mag(self,s,n):
#         import winsound
#         winsound.Beep(s,n)
# z1=clone()
# z1.id=1
# z1.jg=1001
# z1.mag(300,3000)
# print(z1.id,z1.jg)
# z2=clone()
# z2.id=2
# z2.jg=1002
# z2.mag(500,3000)
# print(z2.id,z2.jg)
# z3=clone()
# z3.id=3
# z3.jg=1003
# z3.mag(15000,1000)
# print(z3.id,z3.jg)

#构造方法
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f"姓名：{name}年龄：{age}")
# for i in range(1,3):
#     n=input('姓名：')
#     s=int(input('年龄：'))
#     student(n,s)
#     print(f"当前录入{i}个学生,要录入2位学生")

#魔术方法
# class student:
#     name=None
#     age=None
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"name:{self.name},age:{self.age}"
#     def __lt__(self, other):
#         return self.age<other.age
#     def __le__(self, other):
#         return self.age<=other.age
#     def __eq__(self, other):
#         return self.age==other.age
# s1=student('梨花',22)
# s2=student('苏沫',22)
# print(s1==s2)

#私有和封装继承
class th5g:
    __is5g=0.9
    pasrt_id=1002
    cs=100
    def __chat_5g(self):
        print("正在通话中")
    def chats_5g(self):
        if self.__is5g>=1:
            print("5g打开成功")
        else:
            print('5g打开失败')
            self.__chat_5g()
class Nfc():
    pasrt_id=1003
    __is5g = 1
    cs=99
    def on(self):
        if self.__is5g==1:
            print("打开NFC")
        else:
            print("NFC打开失败")
#重写与调用父类方法
class Phone(th5g,Nfc):
    th5g.cs=102
    def on(self):
        if self._th5g__is5g==1:
            super().on()
            print("成功！")
        else:
            Nfc.on(self)
            print("失败!")

    pass
s=Phone()
s.chats_5g()
s.on()
print(s.cs)