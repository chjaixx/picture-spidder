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
import numpy as np
# import pandas
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
# class th5g:
#     __is5g=0.9
#     pasrt_id=1002
#     cs=100
#     def __chat_5g(self):
#         print("正在通话中")
#     def chats_5g(self):
#         if self.__is5g>=1:
#             print("5g打开成功")
#         else:
#             print('5g打开失败')
#             self.__chat_5g()
# class Nfc():
#     pasrt_id=1003
#     __is5g = 1
#     cs=99
#     def on(self):
#         if self.__is5g==1:
#             print("打开NFC")
#         else:
#             print("NFC打开失败")
# #重写与调用父类方法
# class Phone(th5g,Nfc):
#     th5g.cs=102
#     def on(self):
#         if self._th5g__is5g==1:
#             super().on()
#             print("成功！")
#         else:
#             Nfc.on(self)
#             print("失败!")
#
#     pass
# s=Phone()
# s.chats_5g()
# s.on()
# print(s.cs)
# def fe(data:int)->list:
#     return data*10 #type:int
# print(fe(1))

#多态和抽象类接口
# class Alimony:
#     def spake(self):
#         pass
# class Cat(Alimony):
#     def spake(self):
#         print("喵喵")
# class Dog(Alimony):
#     def spake(self):
#         print("汪汪")
# def ml(alimony:Alimony):
#     alimony.spake()
# cat=Cat()
# dog=Dog()
# ml(cat)
# ml(dog)
# class Kd:
#     def id(self):
#         pass
#     def xh(self):
#         pass
# class xiaomi(Kd):
#     def id(self):
#         print("xiao1003")
#     def xh(self):
#         print("xiaomi手机")
# class relmi(Kd):
#     def id(self):
#         print("relmi1001")
#     def xh(self):
#         print("relmi手机")
# def mege(kd:Kd):
#     kd.id()
#     kd.xh()
# mi=xiaomi()
# relmi=relmi()
# mege(mi)
# mege(relmi)

#mysql的连接
# from pymysql import Connection
# conn=Connection(
#     host='localhost',
#     port=3306,
#     user='root',
#     password='123456'
# )
# print(conn.get_server_info())
# curses=conn.cursor()
# conn.select_db('students')
# # curses.execute("create table test05(id int,info varchar(255))")
# curses.execute("insert into test05 values (1,'code')")
# curses.execute('select * from test')
# test=curses.fetchall()
# for i in test:
#     print(i)
# conn.commit()
# conn.close()

# st_li=[]
# with open('studentP5', 'r', encoding='utf-8') as f:
#     for li in f.readlines():
#         li = li.strip()
#         if not li:
#             continue
#         s=li.sp
#         st_li.append(s)
# print(st_li)

#pyspark
#from fake_useragent import UserAgent
# import os
# os.system('chcp 65001')
# from pyspark import SparkConf,SparkContext
# conf=SparkConf().setMaster("local[*]").\
#     setAppName('test_spark')
# sc=SparkContext(conf=conf)
# print(sc.version)
# sc.stop()
# uangen=UserAgent()
# print(uangen.random)

# import numpy as np
# print(np.__version__)#获取队列的版本号
# arr=np.array([1,2,3,4])#创建一数组
# arr=arr*2
# print(arr)
# print(type(arr))
# arr=np.array([[['a','b','c'],[1,2,3]],
#                 [['d','e','f'],[4,5,6]],
#               [['h','i',' '],[7,8,9]]#队列的列要对齐，如果缺少可以用其他代替
#               ])
# print(arr.ndim)#获取数组的形状
# print(arr.shape)#获取队列的层数，行数，列数
# whar=arr[2,0,2]*3+arr[2,0,0]+arr[1,0,1]
# print(whar)
# arr=np.array([[1,2,3,4],
#               [5,6,7,8],
#               [9,10,11,12],
#               [13,14,15,16]])
# print(arr[1:3])
# print()
# print(arr[::-1])
# print()
# print(arr[:,:1])#取第一列
# print()
# print(arr[2:,:2])#逗号前取行，后取列
# print(arr+1)#numpy可以同时给每个数据都加减乘除平方
# arr=np.array([78.4,56.6,8.001,60.3,90,100])#数据中有一个是小数就全部是小数类型
# print(arr>=60)
# print(np.round(arr))#四舍五入
# print(np.floor(arr))#向下取舍
# print(np.ceil(arr))#向上取舍
# arr[arr<60]=0
# print(np.pi)
# print(arr)

# n,m = map(int,input().split())
# m=2
# n=2
# a = [[0]*(m+2) for _ in range(n+2)] #外圈套0
#
# for i in range(1,n+1):
#     a[i] =list(map(str,input()))
#     a[i][1:-1] =list(map(str,input()))
#
#
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         cnt = 0
#         if a[i][j] != '*':
# 			#判断周围一圈有多少颗地雷“*”
#             for p in range(i-1,i+2):
#                 for q in range(j-1,j+2):
#                     if a[p][q] == '*':
#                         cnt += 1
#             a[i][j] = cnt
#     print("".join(map(str,a[i][1:-1])))
# a[1] =list(map(str,input()))
# a[1][1:-1] =list(map(str,input()))
# print(a)
# n=[[0,0,0,0]]
# n[0]=list(map(str,input()))
# print(n)

#numpy数组之间广播合并为多维数组
# import numpy as np
# arr1=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9]])
# print(np.shape(arr1))
# arr2=np.array([[1,2,3,4,5,6,7,8,9])
# print(np.shape(arr2))
# print(arr2*arr1)#当行数和列数相同时，相乘才能得到一个多维数组9*9乘法表

#numpy的聚合函数
# import numpy as np
# arr=np.array([[1,2,3,4,5],
#              [6,7,8,9,10]])
# print(np.sum(arr))#求和
# print(np.mean(arr))#求平均值
# print(np.std(arr))#求标准差
# print(np.var(arr))#求方差
# print(np.argmin(arr))#求最小值索引
# print(np.argmax(arr))
# print(np.sum(arr,axis=0))#求每一列的和
# print(np.mean(arr,axis=1))#求每一行的平均值

#numpy中进行数据过滤
# import numpy as np
# a=[14,12,19,25,17,18]
# arr=np.array([[14,12,19,25,17,18],
#               [55,34,68,99,76,66]])
# print(np.shape(arr))
# print(arr[arr>=18])
# print(arr[(arr>=18)&(arr<65)])#筛选大于等于18和小于65的
# arr1=arr[arr%2==0]
# print(arr1)
# arr1=arr[arr%2!=0]
# print(arr1)
# arr2=np.where(arr>=18,arr,0)
# print(arr2)

#numpy随机数生成
# import numpy as np
# arr=np.random.default_rng()#构造随机数生成的对象arr
# print(arr.integers(1,10,5))#（整数型）第一个数是随机生成的最小范围数==1，第二个数是随机生成的最大范围数！=10，第三个是随机生成多少个数
# arr2=np.random.default_rng(1)#随机数种子，当使用这个随机数种子时，生成的随机数将不会改变
# print(arr2.integers(1,10,5))
# arr3=np.random.default_rng()
# print(arr3.integers(1,10,(3,4)))#(3,4)代表生成三行四列
# np.random.seed()#主要是设置浮点型随机数的种子可要可不要
# arr4=np.random.uniform(0,3,(3,4))#浮点型
# print(arr4)#浮点型随机数
# arr5=np.array([1,2,3,4,5])
# ang=np.random.default_rng()#ang是个对象
# ang.shuffle(arr5)#打乱arr5这个数组
# print(arr5)
# ang=np.random.default_rng()
# fras=np.array(['石头','剪刀','🙅‍','布'])
# fras=ang.choice(fras,(2,2))#随机选择列表中的已有元素并生成2行2列，或只生成两个元素ang.choice(fras,2)
# print(fras)

#pandas学习
# import pandas as pd
# print(pd.__version__)
# # data=[100,110,112]
# # print(pd.Series(data))#将数组排成列，并在左侧输出从0开始的索引，最后输出数据类型
# # ser=pd.Series(data,index=['a','b','c'])
# # print(ser)#将索引改为abc
# # print(ser.loc['b'])#按标签定位
# # ser.loc['b']=200#修改b标签的数据
# # print(ser)
# # print(ser[ser>=110])
#
# # #通过字典来实现
# # disc={
# #     "Day 1":1768,
# #     "Day 2":1889,
# #     "Day 3":2100
# # }
# # ser1=pd.Series(disc)
# # print(ser1[ser1>2000])
# # ser1.loc["Day 3"]+=200
# # print(ser1.loc["Day 3"])
# # print(ser1)
# # data={
# #     "name":['a','b','c'],
# #     'age':[18,33,22]
# # }
# # df=pd.DataFrame(data,index=['Em1','Em2','Em3'])
# # print(df)
# # print(df.loc['Em1'])#通过标签索引来获取
# # print(df.iloc[0])#通过下标索引来获取
#
# # #添加新的列
# # df['xinbie']=['man','woman','man']
# # print(df)
#
# # #添加新的一行或多行
# # df_new=pd.DataFrame([{"name":'梨花',"age":20,"xinbie":'woman'},{"name":'unge',"age":44,"xinbie":'man'}],
# #                     index=['Em4','Em5'])#新创建一个数组
# # df=pd.concat([df,df_new])#concat将两个数组拼接在一起，只能用于Dataform形式的拼接
# # print(df_new)
# # print(df)
# df=pd.read_csv("data.csv")#读取.csv文件也可以读取.json文件
# print(df)#如果数据量过大这样只能打印前五行和后五行使用df.to_string()可打印全部数据
# pd.DataFrame(df)
# #按列或多列进行选择
# print(df["Name"])
# print(df[["Height","Weight"]])
# #按行或多行进行选择
# #df=pd.read_csv("data.csv",index_col="Name")#使用Name列作为索引标签
# # print(df)
# # print(df.loc["Ivysaur"])
# # print(df.loc[["Venusaur","Ivysaur"]])
# # print(df.loc["Venusaur":"Caterpie",['Height','Weight']])#切片Venusaur到Caterpie的'Height'和'Weight'内容
# # print(df.iloc[0:11:2,0:3])
# # n=input("输入一个精灵的名字：")
# # try:
# #     print(df.loc[n])
# # except Exception as e:
# #     print(f"没有这个精灵{e}")
# # frdf=df[df['Legendary']==False]#选取Legendary=0的数据，当然也可以直接用0
# # print(frdf)
# # frdf=df[(df['Type1']=='Water')|(df['Type2']=='Water')]#或|运算选取以及与运算&
# # print(frdf)
#
# #pandas聚合函数
# print(df.mean(numeric_only=True))#numeric_only=True代表所有数字列
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())
# print(df["Height"].max())
#
# #分组查寻
# df_group=df.groupby('Type1')
# print(df_group['Height'].max())
# print(df_group['Height'].mean())
#
# #数据清洗移除或修复不完整的数据
# #df=df.drop(columns=["No",'Legendary'])#删除列
# #df=df.dropna(subset=['Type2'])#删掉该列中没有数据的行
# # df=df.fillna({'Type2':'None'})#将该列不可用的数据替换为None
# # df['Type1']=df['Type1'].replace({'Grass':'GRASS','Fire':'FIRE',
# #                                  'Watr':'WATER'})#将该列中的对应数据修改
# #将文本标准化
# df['Name']=df['Name'].str.lower()#将Name列全部转为小写
# print(df)
# df['Legendary']=df['Legendary'].astype(bool)#将该列转为bool类型,不能有字符
# print(df)
# df=df.drop_duplicates()#删除重复项
# print(df)

#Acllma值的转换
# x='b'
# x1=ord(x)-32
# print(x1)
# x2=chr(x1)
# print(x2)
# p=[4,3,2,3]
# mai=max(p)
# print(mai)
# print(p.count(mai))

#pandas merge多表合并（merge内似SQL中的join）用于有关联字段的表
# import pandas as pd
# df_stu=pd.DataFrame({
#     'stu_id':[1,2,4,3],
#     'stu_name':['梨花','苏沫','叶海','挽歌']
# })
# df_sco=pd.DataFrame({
#     'stu_id':[1,2,3,5],
#     'scor':[99,87,66,77]
# })
# df_class=pd.DataFrame({
#     'sid':[1,2,3,4],
#     'class_name':['一班','二班','三班','四班']
# })
# res_inner=pd.merge(df_stu,df_sco,on='stu_id',how='inner')#内连接保留关联键一样，on='关联键'，how='连接方式'
# print(res_inner)
# res_left=pd.merge(df_stu,df_sco,on='stu_id',how='left')#无成绩显示NaN
# print(res_left)
# res_diff=pd.merge(df_stu,df_class,left_on='stu_id',right_on='sid',how='left')#当关联键名不一样时
# print(res_diff)
# res=pd.merge(df_stu,df_sco,on=['stu_id','stu_id'])#多字段同时匹配
# print(res)
# res1=pd.merge(df_stu,df_sco,on='stu_id',how='left')
# res2=pd.merge(res1,df_class,left_on='stu_id',right_on='sid',how='left')#三表以上合并，就是链式嵌套
# res2['scor']=res2['scor'].fillna(0)
# print(res2)
# res2.to_csv('stu.csv',index=False,encoding='utf-8',header=False,sep=',')#index=False不导出索引，header=True是否导出表头末日True，sep=','分隔符默认逗号


# n=['1','2','3','4','5']
# l=int(n.pop(0))
# m=int(n.pop(0))
# print(l,m,n)
s='qwert'
s1=list(map(str,s))
print(s1)