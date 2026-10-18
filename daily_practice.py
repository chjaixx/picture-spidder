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
money=8000
for i in range(21):
    import random
    x=random.randint(1,10)
    if x<5:
        print(f"{i}没达标")
        continue
    if x>=5 and money>=1000:
        money-=1000
        print(f'{i}发工资1000公司还剩{money}')
        continue
    else:
        print(f"{i}公司没钱了")
        break






























