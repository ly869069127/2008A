# a = "ahelog"
# l=["a","4","g"]
# t=("a","4","g")
# s={"a","4","g"}
# d = {"name":"王大锤","sex":"女"}
#
# print("a" in a)


# import random
# money = random.randint(0,5000000)
# if money <= 2500000:
#     print("洗洗睡")
# elif money <= 3000000:
#     print("去网吧")
# elif money <= 4500000:
#     print("把老板裁了")
# else:
#     print("买公司")

# for i in range(0,100):
#     print("说100遍")

# print(list(range(10)))
#
# print(list(range(10,0,-5)))
# i=1
# while i <=10:
#     print(i)
#     i += 1
#
# for n in range(10):
#     print(n)

# for i in range(1,101):
#     a = list(str(i))
#     if (a[0] == "5") or (a[1] == "5"):
#         continue
#     print(i)

# i = 0
# while i < 10:
#     i += 1
#     if i == 5 or i == 7:
#         continue
#     print(i)

# a = "54"
# print(list(a))
# b = list(a)
# print(b[0])

# a= 54
# b = str(a)
# print(b+"23")

# for i in range(1,10):
#     for j in range(1,10):
#         print(str(i)+"x"+str(j)+"="+str(i*j))


# def case():
#     print(a)
#     print(b)
# def asd(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# asd(1,5,67,a=1,tt=2)

# b = 20
#
# def su():
#     global b
#     b = 50
#
# su()
# print(b)

# a = '1234567890'
#
# print(a[:6])
# print(a[1:3])
# print(a[:-3])
# print(a[-7:-2])
# print(a[-2:])
# print(a[1:8:2])

# a = '爸爸，儿子，孙子'
# a = a.replace('，',',')
# a = a.split(",")
# print(a)
#
# b = '  sdada   '
# print(b.rstrip())

# for i in range(1,10):
#     for j in range(1,10):
#         print('%d X %d = %d',%(j,i,i*j))
#     print()

# a= [1,5,6,8,41,4,22]
#
# a[1]=10
# a.append(2)
# a.insert(1,60)
# a.extend((1,2,3,4))
# a.pop(1)
# a.remove(1)
# a.sort()
# a.sort(reverse=True)
# print(a)

# a = {'me':'dad','age':'80'}
# a['age'] = 68
# print(a)
# b = {'you':'son','sex':'boy'}
# a.update(b)
# print(a)
# a.pop('sex')
# print(a)
# import random
# a = [random.randint(1,2000) for b in range(100)]
#
# for i in range(len(a)-1,0,-1):
#     for j in range(0,i):
#         if a[j] > a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
# print(a)

# class demo():
#     __a = '类变量'
#     def say(self,value):
#         self.__a = value
#     def look(self):
#         return self.__a
# b = demo()
# b.say('hello')
# print(b.look())
# import requests

# # 1、编写一个返回随机手机号的方法
# import random
# a=[134,135,136,137,138,139,150,151,152,157,158,159,187,188,130,131,132,155,156,185,186,133,153,180,189]
# b=random.choices('1234567890',k=8)
# print(str(random.choice(a))+''.join(b))
# # 2、编写一个返回指定长度和内容的随机字符串方法
# import random
# length = int(input('输入生成随机字符串的长度：'))
# code = input('输入生成随机字符的内容：')
# out = random.choices(code,k=length)
# print(''.join(out))
# # 3、编写一个返回随机姓名的方法
# import random
# xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
# ming = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'
# first_name = str(random.choice(xing))
# a = random.randint(1,2)
# b = random.choices(ming,k=a)
# second_name = ''.join(b)
# print(first_name+second_name)

try：
    1/0
except as e:






