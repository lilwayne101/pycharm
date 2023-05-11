import copy
import random
from filecmp import cmp
import os


import cv2
import numpy as np

# 直接赋值
# a = 3
# 多变量同时赋同一个值
# c = b = 3
# 多变量赋值
# d, e = 2, 3
# 交换变量
# d, e = e, d
# 赋值运算符 ： += -+ *= /= //= **= %=

# 分支
# name = 'bob'
# pwd = '123'
# userName = input("请输入姓名:")
# userPwd = input("请输入密码:")
# if name == userName and pwd == userPwd:
#     print("登录成功")
# elif name != userName:
#     print("无此用户")
# elif pwd != userPwd:
#     print("密码错误")

# 分支嵌套
# while True:
#     score = input("请输入考试成绩(退出登录系统请输入 'quit')：")
#     if score == 'quit':
#         break
#     score = int(score)
#     if 0 <= score <= 100:
#         if score >= 90:
#             print("优")
#             break
#         elif score >= 80:
#             print("良")
#             break
#         elif score >= 60:
#             print("中")
#             break
#         else:
#             print("差")
#             break
#     else:
#         print("考试成绩输入错误,请重新输入！")

# type() 返回值为数据类型
# int() 整型的类型转换
# list() 列表的类型转换
# dict() 字典的类型转换
# str() 字符串的类型转换
# chr() 将变量由ASC||表类型转换为字符
# ord() ASC||表类型转换
# complex() 复数的类型转换
# round() 四舍五入的内置函数
# min()
# max()
# sum()

# 1
# num = int(input("请输入一个整数："))
# if 50 <= num <= 100:
#     print('*******************')
# else:
#     print(num)

# 2
# a = input("请输入一个整数：")
# a = int(a)
# b = input("请再输入一个整数：")
# b = int(b)
# if a > 100 or b > 100:
#     print(a + b - 100)
# else:
#     print(a + b)

# 3
# a = float(input("请输入一个数字："))
# b = float(input("请再输入一个数字："))
# c = input("请输入一个符号：")
# if c == '-':
#     print(a - b)
# if c == '+':
#     print(a + b)
# if c == '*':
#     print(a * b)
# if c == '/':
#     if b != 0:
#         print(a / b)
#     else:
#         print("除数不能为0")
# if c == '//':
#     if b != 0:
#         print(a // b)
#     else:
#         print("除数不能为0")
# if c == '%':
#     if b != 0:
#         print(a % b)
#     else:
#         print("除数不能为0")
# if c == '**':
#     print(a ** b)

# 4
# year = int(input("请输入一个年份："))
# if year % 4 == 0 and year % 100 != 0:
#     print(f"{year}是闰年")
# elif year % 400 == 0:
#     print(f"{year}是闰年")
# else:
#     print(f"{year}不是闰年")

# # 练习
# month = input("请输入一个月份：")
# bigMonth = ['1', '3', '5', '7', '8', '10', '12']
# if month == '2':
#     year = int(input("请输入2月所在的年份："))
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(f"{year}年的{month}月有29天")
#     else:
#         print(f"{year}年的{month}月有28天")
# elif month in bigMonth:
#     print(f"{month}月有31天")
# else:
#     print(f"{month}月有30天")
#
# print("as%ssdadasdaddf" % '1')
#
# # 练习for循环
# total = 0
# for i in range(101):
#     total += i
# print(total)
#
# # 1
# times = 10
# for i in range(times):
#     print("$$$$$$$$")
#
# # 2
# times = 0
# for i in range(1, 101):
#     if i % 3 == 0:
#         print(i, end=' ')
#         times += 1
#         if times == 5:
#             print()
#             times = 0
#
# # 3
# times = int(input("请输入行数："))
# for i in range(times):
#     print('********')
#
# # 4
# total = 0
# for i in range(0, 101, 2):
#     total += i
# print(total)
#
# # 5
# for row in range(1, 10):
#     for col in range(1, row + 1):
#         print(f"{row} * {col} = {row * col}", end='\t')
#     print()
#
# # 6
# for row in range(1, 10):
#     for col in range(1, 10 - row + 1):
#         print(f"{10 - row} * {col} = {(10 - row) * col}", end='\t')
#     print()
#
# # 7
# n = int(input("请输入阶数："))
# sum_nums = 0
# for i in range(1, n + 1):
#     total = 1
#     for j in range(1, i+1):
#         total *= j
#     sum_nums += total
# print(sum_nums)
#
# # 8
# number = 0
# for i in range(4):
#     for j in range(3):
#         for k in range(2):
#             nums = [1, 2, 3, 4]
#             nums.pop(i)
#             nums.pop(j)
#             nums.pop(k)
#             num = i * 100 + j * 10 + k
#             number += 1
#             print(num, end=' ')
# print(number)
#
#
# # 9
# times = 0
# for i in range(100, 201):
#     judgment = 1
#     k = 0
#     for j in range(1, i):
#         if i % j == 0:
#             k += 1
#     if k == 1:
#         print(i, end=' ')
#         times += 1
#         judgment = 0
#     if times % 5 == 0 and judgment == 0:
#         print()
# print('\n'+str(times))
#
# # 10
# times = 5
# for i in range(1, times * 2):
#     if i <= times:
#         print('*' * (i * 2 - 1))
#     else:
#         print('*' * ((times * 2 - i) * 2 - 1))

# # 11
# sum_num = 0
# for i in range(1, 101):
#     total = 0
#     for j in range(1, i + 1):
#         total += j
#     sum_num += total
# print(sum_num)

"""
    day-3
"""
# # 1
# dic = {}
# strRdm = ''.join([chr(random.randint(ord('a'), ord('d'))) for i in range(100)])
# for i in range(ord('a'), ord('d') + 1):
#     dic[chr(i)] = 0
# for s in strRdm:
#     dic[s] += 1
# print(dic)
#
# # 2
# lit = [random.randint(1, 100) for i in range(20)]
# # print(lit)
# reLit = copy.deepcopy(lit)
# for i in range(0, len(lit)):
#     for j in range(0, len(lit)):
#         if lit[i] >= lit[j]:
#             lit[j], lit[i] = lit[i], lit[j]
#         if reLit[i] <= reLit[j]:
#             reLit[j], reLit[i] = reLit[i], reLit[j]
# # lit.sort()
# # reLit.sort(reverse=True)
# print(reLit)
# print(lit)
#
# # 3
# lit = [random.randint(1, 100) for i in range(20)]
# # print(lit)
# reLit = copy.deepcopy(lit)
# i = 0
# while i < len(lit):
#     j = 0
#     while j < len(lit):
#         if lit[i] >= lit[j]:
#             lit[j], lit[i] = lit[i], lit[j]
#         if reLit[i] <= reLit[j]:
#             reLit[j], reLit[i] = reLit[i], reLit[j]
#         j += 1
#     i += 1
# print(lit)
# print(reLit)
#
# # 4
# lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# numInput = int(input("请输入一个整数："))
# times = 1
# for num in lis:
#     times += 1
#     if num == numInput:
#         print("该数已存在")
#         break
#     elif times == len(lis) + 1:
#         print(f"数组中没有{numInput}")
#
# # 5
# while True:
#     listNums = [random.randint(1, 10) for i in range(9)]
#     numInput = int(input("请输入一个整数："))
#     if numInput in listNums:
#         print(listNums)
#         print("数组中存在该数")
#         break
#     print("数组中不存在该数,请重新输入!")
#
# # 6
# score = [random.randint(0, 10) for i in range(10)]
# print("评委分数为：", end='')
# print(score)
# score.sort()
# total = 0
# for i in range(1, len(score) - 1):
#     total += i
# print(f"去掉一个最低分{score[0]},去掉一个最高分{score[-1]},最后得分{total}")

# 7
# stuList = ["bob", "sunny", "jack"]
# classList = ["数学", "语文", "英语", "艺术"]
# scoreList = [[], [], []]
# for index, stu in enumerate(stuList):
#     for indexClass, cls in enumerate(classList):
#         score = int(input(f"请输入{stu}的{cls}成绩"))
#         scoreList[index].append(score)
#     print(f"{stu}的平均分为：{np.mean(scoreList[index])}")
# for index, cls in enumerate(classList):
#     print(f"{cls}的平均分为{np.mean([scoreList[i][index] for i in range(len(scoreList))])}")

# stuList = ["bob", "sunny", "jack"]
# classList = ["数学", "语文", "英语", "艺术"]
# scoreList = []
#
# for index, stu in enumerate(stuList):
#     scores = input(f"请输入{stu}的数学,语文,英语,艺术成绩(请用空格隔开)：")
#     scoreList.append(scores.strip().split(" "))
#     scoreList[index] = [int(score) for score in scoreList[index]]
#     print(f"{stu}的平均分为：{np.mean(scoreList[index])}")
# for index, cls in enumerate(classList):
#     print(f"{cls}的平均分为{np.mean([scoreList[i][index] for i in range(len(scoreList))])}")
# print(scoreList)

"""
    day-4
"""
# random.seed(1)  # 随机种子 只随机一次
# a = [(random.randint(1, 100), i) for i in range(10) if i > 5]
# print(a)

# random.random() # 随机返回一个0-1之间的数
# a = [round(random.random() * 100, 2) for i in range(10)]
# a = ["%.2f" % (random.random() * 100) for i in range(10)]

# [a, b] = {"1": 2, "2": 3}  # 1 2

# stuList = ["bob", "sunny", "jack"]
# classList = ["数学", "语文", "英语", "艺术"]
# scoreList = []
#
# for index, stu in enumerate(stuList):
#     scores = input(f"请输入{stu}的数学,语文,英语,艺术成绩(请用空格隔开)：")
#     scoreList.append(scores.strip().split(" "))
#     scoreList[index] = [int(score) for score in scoreList[index]]
#     print(f"{stu}的平均分为：{np.mean(scoreList[index])}")
# for index, cls in enumerate(classList):
#     print(f"{cls}的平均分为{np.mean([scoreList[i][index] for i in range(len(scoreList))])}")
# print(scoreList)

# string = 'asdsf123AS\nDF'
# print(string.capitalize())
# print(string.count('a'))
# print(string.endswith('F'))
# print(string.find('d'))
# print("我是{0}，我今年{1}岁，小名是{0}".format('bob', 18))
# print(string.index('s'))
# print(string.isalnum())
# print(string.isalpha())
# print(string.isdecimal())
# print(string.isdigit())
# print(string.islower())
# print(string.isnumeric())
# print(string.isspace())
# print(string.istitle())
# print(string.isupper())
# print(string.join('123'))
# print(string.ljust(20))
# print(string.lstrip())
# print(len(string))
# print(max(string))
# print(min(string))
# print(string.partition('123'))
# print(string.replace('123', '456'))
# print(string.rfind('123'))
# print(string.rindex('123'))
# print(string.rjust(20))
# print(string.rpartition("123"))
# print(string.rstrip())
# print(string.split('123'))
# print(string.splitlines())
# print(string.startswith('a'))
# print(string.strip())
# print(string.swapcase())
# print(string.title())
# print(string.upper())
# print(string.zfill(20))

# 列表的定义
# a = [1, 2, 3]
# b = []
# c = list()

# 列表的添加
# a.append(b)
# b.append('1')
# a.insert(1, '2')
# a.extend(b)

# 列表的删除
# del c
# a.remove('1')
# a.pop(1)
# print(a)  # [1, 2, 3, ['1']]
# print(a.pop())  # ['1']
# b.clear()

# 列表的修改
# a[1] = '2'

# 列表的查询
# print(a[1])
# a.index('2')
# print(len(a))
# print(a.count("2"))

# 列表的排序
# a.sort()
# a.sort(reverse=True)
# a.reverse()

# 切片
# listA = [i for i in range(10)]
# print(listA[::2])
# print(listA[::-2])

# 练习
# a = np.array(range(25)).reshape((5, 5)).tolist()  # tolist() 变为列表
# print(type(a))
# b = [1, 2]
# c = [3, 4]
# a = b + c
# print(a * 2)
# print(type(enumerate(a)))
#
# a = [[1, 2, 3], [2, 3, 4]]
# a.reverse()  # [[2, 3, 4], [1, 2, 3]]
# c = zip([1, 2, 3], [5, 6, 7])
# print(c)
# for a, b in zip([1, 2, 3], [5, 6, 7]):
#
# x = [1, 2, 3]
# y = [4, 5, 6]
# w = 1
# b = 2
# loss = []
# for x1, y1 in zip(x, y):
#     y2 = w * x1 + b
#     loss.append(y1 - y2)
# print(loss)

# 元组的定义
# a = ()
# b = tuple()
#
# c = (16,)
# print(c)

# 练习
# a = ([1, 23], [2])  # 元组的元素不能修改
# a[0][1] = 50  # 但是元组的元素的元素 不是元组的元素
# print(a)  # ([1, 50], [2])

# 深拷贝
# a = copy.deepcopy(b)

# 字典的定义
# dic = {"bob": 18, "jack": 19, "sunny": 20}
# dic1 = {"james": 40}

# 值可以是任意类型 但键不可变 只能使字符串 数字 元组

# 字典的修改
# dic['bob'] = 20
# dic.setdefault("lil ZZ", 20)
# dic.update(dic1)

# 字典的删除
# del dic['bob']
# # dic.pop('bob')
# dic1.clear()

# 字典的查询
# print(dic["james"])
# print(dic.get("sunny"))
# print(len(dic))
# print(list(dic.values()))
# print(tuple(dic.keys()))
# print("sunny" in dic)

# 1
# shopList = [[], [], []]
# goodList = ["小米", "苹果", "华为", "西瓜", "土豆", "牛奶"]
# for i in range(len(goodList)):
#     shopList[random.randint(0, 2)].append(goodList[i])
# print(shopList)

# 2
# shopList = {"小米商城": [], "苹果商城": [], "华为商城": []}
# goodList = ["小米", "苹果", "华为", "西瓜", "土豆", "牛奶"]
# for i in range(len(goodList)):
#     shopList[[key for key in list(shopList.keys())][random.randint(0, len(shopList) - 1)]].append(goodList[i])
# print(shopList)

# 3
# while True:
#     # 输入日期并判断格式
#     date = input("该版本只适用于公元1000年以后及公元10000以前\n请输入日期(年月日 以空格隔开 示例：2008 8 8)：")
#     date = date.splitlines()
#     date = ' '.join(date)
#     date.strip()
#     if len(date) > 11:
#         print("输入的日期格式错误,请按照示例格式输入日期!")
#         continue
#     listTemp = [date[0:4], date[4:7], date[7:10]]
#     # print(date)
#     dateList = [var.strip() for var in listTemp]
#     judgment = [dateList[i].isdecimal() for i in range(len(dateList))]
#     # print(dateList)
#     # print(judgment)
#     if not (judgment[0] and judgment[1] and judgment[2]):
#         print("输入的日期格式错误,请按照示例格式输入日期!")
#         continue
#     dateList = [int(var) for var in dateList]
#     bigMonth = [1, 3, 5, 7, 8, 10, 12]
#     leapYear = 0
#     if (dateList[0] % 4 == 0 and dateList[0] % 100 != 0) or dateList[0] % 400 == 0:
#         leapYear = 1
#     # 判断日期是否存在
#     if dateList[1] == 2 and dateList[2] > 29 and leapYear == 1:
#         print("Error1:该日期不存在,请重新输入!")
#         continue
#     elif dateList[1] == 2 and dateList[2] > 28 and leapYear == 0:
#         print("Error2:该日期不存在,请重新输入!")
#         continue
#     elif dateList[1] > 12 or dateList[2] > 31:
#         print("Error3:该日期不存在,请重新输入!")
#         continue
#     elif (dateList[1] > 12 or dateList[2] == 31) and dateList[1] not in bigMonth:
#         print("Error4:该日期不存在,请重新输入!")
#         continue
#     # 计算下一天的日期
#     if dateList[1] == 2 and dateList[2] == 28 and leapYear == 1:
#         dateList[2] += 1
#     elif dateList[1] == 2 and dateList[2] == 29 and leapYear == 1:
#         dateList[1] += 1
#         dateList[2] = 1
#     elif dateList[1] == 2 and dateList[2] == 28 and leapYear == 0:
#         dateList[1] += 1
#         dateList[2] = 1
#     elif dateList[1] in bigMonth and dateList[2] == 31 and dateList[1] == 12:
#         dateList[1] = 1
#         dateList[2] = 1
#         dateList[0] += 1
#     elif dateList[1] in bigMonth and dateList[2] == 31:
#         dateList[1] += 1
#         dateList[2] = 1
#     elif dateList[1] not in bigMonth and dateList[2] == 30:
#         dateList[1] += 1
#         dateList[2] = 1
#     else:
#         dateList[2] += 1
#     print(dateList)
#     break

"""
    Day-5
"""


# def 函数名(形参1,.....)
#     pass

#
# # 函数定义
# def a():
#     print("bob")
# # 函数的调用
# a()


# def a():
#     return 4, 5, 6
#
#
# print(a())
# print(type(a))
# print(type(a()))
# b = a()
# print(b)
# a, b, c = a()
# print(a)

# 全局变量 global a 用于在函数内部修改全局变量
# 局部变量 只能在函数内使用 不能在函数外部调用


# 1
# def calculate(a, c, b):
#     if c == '-':
#         return a - b
#     if c == '+':
#         return a + b
#     if c == '*':
#         return a * b
#     if c == '/':
#         if b != 0:
#             return a / b
#         else:
#             return "除数不能为0"
#     if c == '//':
#         if b != 0:
#             return a // b
#         else:
#             return "除数不能为0"
#     if c == '%':
#         if b != 0:
#             return a % b
#         else:
#             return "除数不能为0"
#     if c == '**':
#         return a ** b
#
#
# # calculate(2, '*', 5)
#
# tuple_nums = (1, 2, 3, 4, 5, 6)
#
#
# def mean(tuple_num):
#     mean_num = 0
#     for i in tuple_num:
#         mean_num += i
#     return mean_num / len(tuple_num)
#
#
# print(mean(tuple_nums))
#
#
# def sum_num(tuple_num):
#     total = 0
#     for i in tuple_num:
#         total += i
#     return total
#
#
# print(sum_num(tuple_nums))

# def num(a: str):    # 必要参数
#     print(type(a))
#     print(a)
#
#
# def nums(**dict_num):
#     print(type(dict_num))
#     print(dict_num)
#
#
# nums(name="bob", age="17")
# num(19)

# 匿名函数
# fo = lambda a, b: a + b
# print(fo(1, 2))

# 2
# def sum_nums(a, b, c):
#     return print(a + b + c)
#
#
# sum_nums(1, 2, 3)


# 3
# def max_nums(a, b, c):
#     if a >= b and a >= c:
#         return a
#     if b >= a and b >= c:
#         return b
#     if c >= b and c >= a:
#         return c
#
#
# print(max_nums(1, 2, 3))
#
#
# # 4
# def min_nums(a, b, c):
#     if a <= b and a <= c:
#         return a
#     if b <= a and b <= c:
#         return b
#     if c <= b and c <= a:
#         return c
#
#
# print(min_nums(1, 2, 3))

# 5
# num_list = [10, 20, 30, 40, 50]
#
#
# def index(num, nums):
#     if num not in nums:
#         return "列表中无此元素！"
#     else:
#         temp_index = 0
#         for ele in nums:
#             if num == ele:
#                 return temp_index
#             else:
#                 temp_index += 1
#
#
# print(index(6, num_list))
# print(index(20, num_list))

# 6

# def msg_input():
#     name = input("请输入姓名：")
#     sex = input("请输入性别：")
#     addr = input("请输入家庭地址：")
#     return {"姓名": name, "性别": sex, "家庭住址": addr}
#
#
# def msg_print(msg_temp):
#     print(msg_temp)
#
#
# msg_print(msg_input())

# 7
# def fun(num):
#     for row in range(1, num+1):
#         for col in range(1, row + 1):
#             print(f"{row} * {col} = {row * col}", end="\t")
#         print()
#
#
# fun(9)

# 8
# def fact(num):
#     total = 1
#     for i in range(1, num + 1):
#         total *= i
#     return total
#
#
# def total_fact(num):
#     total = 0
#     for i in range(1, num + 1):
#         total += fact(i)
#     return total
#
#
# print(fact(3))
# print(total_fact(3))

# 9
# cards = [{"name": "bob", "age": 18, "sex": "男", "tel": 15465456151, "addr": "北京"}]
#
#
# def add_card():
#     global cards
#     print("正在添加名片...")
#     card = {"name": input("请输入名字："), "age": input("请输入年龄："), "sex": input("请输入性别："),
#             "tel": input("请输入电话："), "addr": input("请输入地址：")}
#     cards.append(card)
#     return card
#

# def revise_card():
#     global cards
#     print("正在修改名片...")
#     rename = input("请输入需要修改名片的名字:")
#     judgment = 0
#     for index, card in enumerate(cards):
#         if rename in card.values():
#             card = add_card()
#             cards.pop(-1)
#             cards[index] = card
#         else:
#             judgment += 1
#     if judgment == len(cards):
#         print("无此人")
#
#
# def print_card():
#     global cards
#     print("正在输出名片...")
#     for index, card in enumerate(cards):
#         print(f"姓名：{card['name']}\t年龄:{card['age']}\t性别:{card['sex']}
#         \ttel:{card['tel']}\taddr:{card['addr']}")
#     pass
#
#
# add_card()
# revise_card()
# print_card()

# 10
# def count(month: int):
#     num = [1, 1]
#     if month < 2:
#         return 2
#     else:
#         for m in range(2, month):
#             num.append(num[m - 1] + num[m - 2])
#             print(num)
#     return num[-1]
#
#
# print(count(10))


# def count(month: int):
#     if month > 2:
#         total = count(month - 1) + count(month - 2)
#         return total
#     else:
#         return 1
#
#
# print(count(10))

"""
    面向对象
"""


# class Stu:
#     name: str = 'bob'
#     age: int = 12
#
#
# # 主程序入口
# if __name__ == '__main__':
#     stu = Stu()
#     print(stu)


# class Score:
#     num = 3
#
#     # 初始化对象属性
#     def __init__(self, math, chinese, english):
#         self.math = math
#         self.chinese = chinese
#         self.english = english
#
#     # def __getattr__(self, item):
#     #     return self.class_list[item]
#
#
# class Student:
#
#     # 初始化对象属性
#     def __init__(self, name, age, score: Score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#
# class Students:
#     stu_list = []
#     stu_dict_list = []
#
#     # 添加学生信息
#     def add_stu(self, stu: Student):
#         Students.stu_list.append(Student(stu.name, stu.age, stu.score))
#
#     # 输出学生信息
#     def stus_info(self):
#         stu_dict = {}
#         for index, stu_info in enumerate(Students.stu_list):
#             stu_dict["姓名"] = stu_info.name
#             stu_dict["年龄"] = stu_info.age
#             stu_dict["数学成绩"] = stu_info.score.__dict__["math"]
#             stu_dict["语文成绩"] = stu_info.score.__dict__["chinese"]
#             stu_dict["英语成绩"] = stu_info.score.__dict__["english"]
#             Students.stu_dict_list.append(stu_dict)
#             print(stu_dict)
#         return Students.stu_dict_list
#
#     # 学生列表长度
#     def __len__(self):
#         return len(Students.stu_list)
#
#
# class Operate(Students):
#
#     # 单个学生平均成绩
#     def stu_mean(self):
#         list_stu = []
#         len_temp = Score.num
#         for index, stu_info in enumerate(Students.stu_list):
#             list_stu.append(sum(list(stu_info.score.__dict__.values())) / len_temp)
#             print(f"{stu_info.name}的平均成绩为：{list_stu[index]}")
#         return list_stu
#
#     # 全班学生平均成绩
#     def stus_mean(self):
#         len_temp = len(Students.stu_list)
#         mean = [float(0) for i in range(len_temp)]
#         for index, stu_info in enumerate(Students.stu_list):
#             i = 0
#             for key, value in stu_info.score.__dict__.items():
#                 mean[i] += value / len_temp
#                 mean[i] = round(mean[i], 2)
#                 i += 1
#
#         # print(f"所有学生的数学平均成绩为：{mean[0]}\n所有学生的语文平均成绩为：{mean[1]}\n所有学生的英语平均成绩为：{mean[2]}")
#         return mean
#
#
# student = Students()
# student.add_stu(Student('bob', 19, Score(89, 88, 87)))
# student.add_stu(Student('sunny', 12, Score(86, 98, 86)))
# student.add_stu(Student('jack', 13, Score(90, 76, 53)))
# student.stus_info()
# op = Operate()
# op.stu_mean()
# print(op.stus_mean())

"""
    创建一个学校 科目 班级 老师 学生
    求：老师最高工资，平均工资，最低工资，每个老师上的科目，带的班级是什么
    每个学生学的科目是什么老师 平均成绩 最擅长科目
"""
import json
# from course_code_package.school import School
# from course_code_package.teacher import Teacher
# from course_code_package.student import Student
# # from course_code_package.subject import Subject
# from course_code_package.operate import Operate
# from course_code_package.class_stu import Class
# from course_code_package.data_read_write import DataReadWrite
#
#
# class_dic_init = {
#     "一班": [["一班", '小王', '男', {"数学": 89, "语文": 88, "英语": 90}],
#              ["一班", '小周', '男', {"数学": 79, "语文": 78, "英语": 70}]],
#     '二班': [["二班", '小李', '男', {"数学": 87, "语文": 98, "英语": 98}],
#              ["二班", '小朱', '女', {"数学": 99, "语文": 90, "英语": 98}]],
#     '三班': [["三班", '小马', '男', {"数学": 67, "语文": 78, "英语": 88}],
#              ["三班", '小赵', '女', {"数学": 69, "语文": 80, "英语": 88}]],
#     '四班': [["四班", '小刘', '男', {"数学": 68, "语文": 98, "英语": 78}],
#              ["四班", '小孙', '女', {"数学": 99, "语文": 66, "英语": 78}]]
# }
#
# teacher_list_init = {
#     '1': ['张老师', 4566, "数学", ["一班", '三班']],
#     '2': ['王老师', 7456, "数学", ["二班", '四班']],
#     '3': ['赵老师', 9879, "语文", ["一班", '二班']],
#     '4': ['钱老师', 2345, "语文", ["二班", '四班']],
#     '5': ['孙老师', 5675, "英语", ["一班", '二班']],
#     '6': ['李老师', 10933, "英语", ["二班", '四班']],
# }
#
# student_list_init = {
#     '1': ["一班", '小王', '男', {"数学": 89, "语文": 88, "英语": 90}],
#     '2': ["一班", '小周', '男', {"数学": 79, "语文": 78, "英语": 70}],
#     '3': ["二班", '小李', '男', {"数学": 87, "语文": 98, "英语": 98}],
#     '4': ["二班", '小朱', '女', {"数学": 99, "语文": 90, "英语": 98}],
#     '5': ["三班", '小马', '男', {"数学": 67, "语文": 78, "英语": 88}],
#     '6': ["三班", '小赵', '女', {"数学": 69, "语文": 80, "英语": 88}],
#     '7': ["四班", '小刘', '男', {"数学": 68, "语文": 98, "英语": 78}],
#     '8': ["四班", '小孙', '女', {"数学": 99, "语文": 66, "英语": 78}]
# }
#
# # 写数据
# path_temp = r"./course_code_data_file"
# data_r_w = DataReadWrite()
# # data_r_w.data_write(teacher_list, path_temp + '//' + 'teacher_data')
# # data_r_w.data_write(student_list, path_temp + '//' + 'student_data')
# # data_r_w.data_write(class_dic, path_temp + '//' + 'class_data')
#
# # 读数据
# t = data_r_w.data_read(path_temp + '//' + 'teacher_data')
# teacher_list_temp = [t[str(i)] for i in range(1, len(t) + 1)]
# s = data_r_w.data_read(path_temp + '//' + 'student_data')
# student_list_temp = [s[str(i)] for i in range(1, len(s) + 1)]
# class_list = data_r_w.data_read(path_temp + '//' + 'class_data')
#
# # print(class_list)
# # 创建对象
# op = Operate()
# class_list = op.create_class_list(class_list)
# print(class_list)
# student_list = op.create_student_list(student_list_temp)
# print(student_list)
# teacher_list = op.create_teacher_list(teacher_list_temp)
# print(teacher_list)
#
# print(op.max_salary(teacher_list))
# print(op.min_salary(teacher_list))
# print(op.mean_salary(teacher_list))
# op.show_teacher(teacher_list)
# op.stu_teacher(student_list, teacher_list)
# op.mean_score_stu(student_list)
# op.good_at_sub(student_list)


# 常用的魔法方法
# __dict__ 字典化对象属性
# class Abc:
#     list1 = []
#     b = 12
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.data = {}
#
#
#     # 调用不存在的属性时自动调用
#     def __getattr__(self, item):
#         return print(f"不存在{item}")
#         pass
#
#     # 定义一次对象成员时 自动调用一次
#     def __setattr__(self, key, value):
#         print("调用setattr")
#         self.__dict__[key] = value
#
#     # 将实例对象以列表形式调用时自动调用
#     def __getitem__(self, item):
#         print(item)
#
#     # 将对象以列表形式赋值(字典赋值)时自动调用
#     # 类似
#     def __setitem__(self, key, value):
#         print("调用setitem")
#         self.__dict__[key] = value
#
#
# a = Abc('BOB', 12)
# # print(Abc[2])
# a['jab'] = 'mouse'
# # print(a['jab'])

# print(a.list1)
# #
# print(a.__dict__)
# print(len(a.__dict__))
# print(Abc.__dict__)
# print(len(Abc.__dict__))
# # 示例化的对象是一个拥有类属性的独立对象
# print(a.b)
# a.b = 100
# # 示例化的对象可以对自己拥有的原来的类属性进行修改
# print(a.b)
# # 示例化的对象对无法类的属性进行修改
# print(Abc.b)
# Abc.b = 1000
# print(Abc.b)


# 常量
# ABC_CORE = 111

# 引入模块
# import 模块名

# 引入模块中的类并改名
# from 模块名 import 类名 as 新类名

# __init__中存放引用包时自动执行的代码

# json格式
# import json
# a = {"bob": "kk"}
# # json字符串
# s = json.dumps(a)
# print(type(s))
# a1 = json.loads(s)
# print(a1)
# print(type(a1))

# with open("./course_code_data_file/data", 'a+', encoding="utf-8") as file:
#     strs = 'wo shi ni'
#     file.write(strs)
#     file.seek(0)
#     data = file.readline()
# print(data)

# eval()将字符串转换为代码运行并返回运行的结果
# def f(q):
#     print(q)
#
#
# b = 'f'
# a = f'f(55)'
# eval(a)

# class Stu:
#     # 类属性 每个实例化对象都有 且初始值相同 要求对所有对象同时进行操作时则定义成类属性
#     class_stu = "一年级"
#
#     def __init__(self, name):
#         # 对象成员
#         self.name = name
#
#     def __call__(self, *args, **kwargs):
#         self.id = '101'
#         return self
#
#     # 静态方法不用传对象self
#     @staticmethod
#     def test1():
#         print("调用test1静态方法")
#
#     # 类方法可以调用类中其他的方法
#     @classmethod
#     def test2(cls):
#         print(f"{cls.class_stu}")
#         cls.test1()
#         Stu.test1()
#         print("调用test2类方法")
#
#
# stu = Stu('Bob')
# stu.test1()
# stu.test2()

# class Goods:
#     def __init__(self, title, price, num):
#         self.title = title
#         self.price = price
#         self.num = num
#
#     def sell(self):
#         pass
#
# class Shoes(Goods):
#     def __init__(self, title, price, num, size):
#         super().__init__(title, price, num)
#         self.size = size
#
#     def sell(self):
#         print("")

"""
要求:

1. 定义基类Person,表示人,有姓名、年龄等属性。

2. 定义Customer类继承Person,表示顾客,有购物车属性,以及购物相关方法。

3. 定义Cashier类继承Person,表示收银员,有收银台属性,以及结账方法。 

4. 定义Goods作为商品类别树的根节点。有Food、Appliance等子类别。每个类别都有价格、库存等属性,以及出售方法。

5. 定义Order类,表示订单,有下单时间、送货时间、订单状态以及包含的商品列表属性。与顾客和配送员关联。

6. 定义Courier类继承Person,表示配送员,有送货清单和送货时间属性,以及送货方法。

7. Mall类包含人员列表、商品类别树、订单列表,以及添加商品类别、添加人员、生成订单、配送订单等方法。

8. 系统支持添加商品类别、人员和商品。删除时需要级联更新相关信息。

9. 选购商品时可以在所有子类别中选择。结账时生成订单,送货前标记为“未送货”,送货后“已送货”,
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Goods:
    def __init__(self, name, price, num_stock):
        self.name = name
        self.price = price
        self.num_stock = num_stock
        self.type = 'others'

    def sell(self):
        self.num_stock -= 1


class Food(Goods):
    def __init__(self, name, price, num_stock):
        super().__init__(name, price, num_stock)
        self.type = 'food'


class Appliance(Goods):
    def __init__(self, name, price, num_stock):
        super().__init__(name, price, num_stock)
        self.type = 'appliance'


class Customer(Person):
    def __init__(self, name, age, shopping_cart: list):
        super().__init__(name, age)
        self.shopping_cart = shopping_cart

    def shopping(self, goods: Goods):
        self.shopping_cart.append(goods)
        return print(f"已将{goods}添加至{self.name}的购物车")


class Cashier(Person):
    def __init__(self, name, age, checkout_counter):
        super().__init__(name, age)
        self.checkout_counter = checkout_counter
        self.count = 0

    def bill(self, customer: Customer):
        i = 0
        print(f"顾客：{customer.name}")
        for goods in customer.shopping_cart:
            i += 1
            print(f"{i}:{goods.name}----{goods.price}元")
            self.count += goods.price
        print(f"共计：{self.count}元")


class Courier(Person):
    def __init__(self, delivery_order, delivery_time, name, age):
        super().__init__(name, age)
        self.delivery_order = delivery_order
        self.delivery_time = delivery_time
        self.status = "未发货"

    def delivery(self, goods):
        self.status = "已发货"
        print(f"{goods}：{self.status}")


class Order:
    def __init__(self, order_time, delivery_time, order_status, order_goods_list):
        self.order_time = order_time
        self.delivery_time = delivery_time
        self.order_status = order_status
        self.order_goods_list = order_goods_list

    def read_order_data(self, path):
        with open(path, "r", encoding="utf-8") as data_order:
            data_order = json.loads(data_order.read())
        return data_order

    def create_order_list(self, order_data):
        order_list = []
        for index, order in order_data.items():
            order_list.append(Order(order["order_time"], order["delivery_time"],
                                    order["order_status"], order["order_goods_list"]))
        return order_list

    def connection(self, courier: Courier):
        print(f"{courier.status}")

class Mall:
    def __init__(self, personnel_dic, commodity_category_dic, order_list):
        self.personnel_dic = personnel_dic
        self.commodity_category_dic = commodity_category_dic
        self.order_list = order_list

    def add_commodity_cate(self, goods):
        self.commodity_category_dic[goods.type].append(goods)
        return self.commodity_category_dic

    def add_person(self, person):
        self.personnel_dic[person.__name__].append()
        return self.personnel_dic

    def product_order(self):
        pass

    def shipping_order(self):
        pass


# python 操作文件夹的方法和规则
import os

# os.listdir()列出文件夹中的文件和子文件
path = r"/course_code_package"
# folder_list = os.listdir(path)
# print(folder_list)

# os.mkdir()创建文件 创建在当前文件目录下
# os.mkdir("test")

# os.makedirs()创建多层文件夹
# os.makedirs("path/to/somedir")

# os.rmdir()删除空文件夹
# os.rmdir("path")

# os.rename(old, new) 重命名/移动 文件夹 (注意：)路径名
# os.rename('test', 'test1')

# os.rename("test", r"./course_code_package/tws3")

# shutil.rmtree()删除非空文件夹
# import shutil
# shutil.rmtree("./course_code_package/tws3")

# os.chdir()改变当前工作目录
# os.chdir("course_code_package")
# print(os.getcwd())
# os.chdir("../")
# print(os.getcwd())

# os.path.isabs()检查是否是绝对路径
# print(os.path.isabs("python_pycharm/Day_14"))
# print(os.path.isabs("/python_pycharm/Day_14"))

# os.path.exists(path) 检查路径是否存在
# print(os.path.exists(path))

# os.path.getsize(file) 获取文件大小
# print(os.path.getsize("./course_code_package/class_stu.py"))

# 返回路径的基名称 os.path.basename(path)
# print(os.path.basename("./course_code_package/class_stu.py"))

# os.path.dirname(path):返回路径的目录名称
# print(os.path.dirname(path))

# os.path.join(path1, path2, ...) 将多个路径拼接成完整路径
# path1 = 'class_stu.py'
# print(os.path.join(path, path1))

# 返回绝对路径
# print(os.path.abspath("practice.py"))

# 一个进程里面可以包含多个线程
# 根本目的是提高工作效率

import time
import threading
# def test(a, b):
#     while True:
#         # print(a, b)
#         print(threading.current_thread())
#         print(time.time())
#         time.sleep(1)
# def test2(a, b):
#     while True:
#         # print(a, b)
#         time.sleep(1)
#
# th1 = threading.Thread(target=test, args=("Theard_test", 1), name="thread-1")
# th1.start()
# # print(threading.current_thread().name)
# th2 = threading.Thread(target=test, args=("Theard_test", 2), name="thread-2")
# th2.start()
# print(threading.current_thread().name)

# 多线程并行和锁
# current_thread = 1
#
#
# class th(threading.Thread):
#
#     def __init__(self):
#         super().__init__()
#         self.run1 = threading.Thread(target=self.run1)
#         self.condition1 = threading.Condition()
#         self.run2 = threading.Thread(target=self.run2)
#         self.condition2 = threading.Condition()
#         self.run3 = threading.Thread(target=self.run3)
#         self.condition3 = threading.Condition()
#
#     def run(self):
#         self.run1.start()
#         self.run2.start()
#         self.run3.start()
#         self.run1.join()
#         self.run2.join()
#         self.run3.join()
#
#     def run1(self):
#         global current_thread
#         with self.condition1:
#             while current_thread != 1:
#                 self.condition1.wait()
#             for i in range(20):
#                 print("run1")
#                 time.sleep(0.1)
#             current_thread += 1
#             self.condition1.notify()
#
#     def run2(self):
#         global current_thread
#         with self.condition2:
#             while current_thread != 2:
#                 self.condition2.wait()
#             for i in range(20):
#                 print("run2")
#                 time.sleep(0.1)
#             current_thread += 1
#             self.condition2.notify()
#
#     def run3(self):
#         global current_thread
#         with self.condition3:
#             while current_thread != 3:
#                 self.condition3.wait()
#             for i in range(20):
#                 print("run3")
#                 time.sleep(0.1)
#             current_thread += 1
#             self.condition3.notify()
#
# th().start()

# def display(count):
#     for i in range(1, count + 1):
#         print(i, end="")
#         time.sleep(1)


# 异常
# a = [1]
#
# try:
#     print(a[0])
# except Exception as e:
#     print(e)
# else:
#     print("test successfully")
# finally:
#     print("test over")

# 作业
# 初始化50个商品
from threading import Timer

# lock = threading.RLock()
# lock1 = threading.RLock()
# lock2 = threading.RLock()
#
#
# def is_jason(string):
#     try:
#         json.loads(string)
#         return True
#     except:
#         return False
#
#
# path = os.path.join(os.getcwd(), 'test.txt')
#
#
# class Goods:
#     total_dic = {"商品数量": 50}
#
#     @classmethod
#     def write_file_goods(cls, path):
#         if not os.path.exists(path):
#             return "文件路径不存在"
#         lock2.acquire()
#         with open(path, 'w', encoding='utf-8') as w_file:
#             data = json.dumps(cls.total_dic)
#             w_file.write(data)
#         lock2.release()
#
#     @classmethod
#     def read_file_goods(cls, path):
#         if not os.path.exists(path):
#             return "文件路径不存在"
#         with open(path, 'r', encoding='utf-8') as w_file:
#             w_file.seek(0)
#             lock2.acquire()
#             data = w_file.read()
#             if not is_jason(data):
#                 print(data)
#                 print("读取到非json内容")
#             data = json.loads(data)
#             lock2.release()
#             return data
#
#
# class Add(threading.Thread):
#
#     def __init__(self):
#         super().__init__()
#         # 添加商品的线程
#         self.add_thread = threading.Thread(target=self.run)
#
#     def run(self):
#         lock2.acquire()
#         i = 0
#         while i < 100:
#             random.seed()
#             dic_read = Goods.read_file_goods(path)
#             num = random.randint(1, 10)
#             try:
#                 total_dic = {"商品数量": num + int(dic_read["商品数量"])}
#             except Exception as e:
#                 print(e)
#             else:
#                 total_dic = {"商品数量": num + int(dic_read["商品数量"])}
#             print(f"新到货{num}件,目前库存{total_dic['商品数量']}件,大家快来买啊！")
#             Goods.write_file_goods(path)
#             time.sleep(1)
#             i += 1
#         lock2.release()
#
#
# class Sell_goods(threading.Thread):
#     def __init__(self):
#         super().__init__()
#         self.sell_thread1 = threading.Thread(target=self.sell_goods, name="一号店铺")
#         self.sell_thread2 = threading.Thread(target=self.sell_goods, name="二号店铺")
#         time.sleep(2)
#
#     def sell_goods(self):
#         i = 0
#         while i < 100:
#             lock.acquire()
#             data = Goods.read_file_goods(path)
#             time.sleep(1)
#             random.seed()
#             buy_nums = random.randint(1, 10)
#             print(f"有人在{threading.currentThread().name}购买{buy_nums}件商品")
#             lock.release()
#             if (data["商品数量"] - buy_nums) < 0:
#                 print("库存不足,请重新购买")
#                 continue
#             lock.acquire()
#             data['商品数量'] -= buy_nums
#             print(f"购买成功，库存余量{data['商品数量']}")
#             Goods.total_dic['商品数量'] = data['商品数量']
#             Goods.write_file_goods(path)
#             lock.release()
#             i += 1
#         print(f"{threading.currentThread().name}卖完咯")


#     def run(self):
#         self.sell_thread1.start()
#         self.sell_thread2.start()

# good = Goods()
# good.write_file_goods(path)
# good.read_file_goods(path)
# sell = Sell_goods()
# sell.start()
# add = Add()
# add.start()

"""
需求：
1.商品的创建
2.库房数据的读写
3.添加商品入库
4.用户类，用户购买商品出库
5.创建同步器
6.给用户和库房设计余额，
库房添加商品需要扣除钱，
用户购买需要扣除钱，
用户不定时增加不定额的钱
"""

# from goods_stock import Goods
# from file import File
# from users import User
#
# goods = Goods()
# goods.create_goods_stock()
# goods.show_goods_stock()
# file = File()
# user = User()

# a = []
# for i in range(100000000):
#     a.append(random.random())
# t1 = time.time()
# s = sum(a)
# t2 = time.time()
# print(t2 - t1)
#
# b = np.array(a)
# t3 = time.time()
# s1 = np.sum(b)
# t4 = time.time()
# print(t4 - t3)

# 三维运算符
# a = np.array([0 if i % 2 else 1 for i in range(10)])
# print(a)
# # 查看数据结构
# print(a.shape)
# # 维度
# print(a.ndim)
# # 元素的数量
# print(a.size)
# # 元素的数据类型
# print(a.dtype)

# print(np.random.normal(0, 2, (3, 3)))
# l = []
# for times in range(4):
#     l.append([i % 2 for i in range(8)])
#     l.append([i % 2 for i in range(1, 9)])
# a = np.array(l)
#
# h, w = a.shape
# board = np.full(shape=[800, 800, 3], fill_value=(0, 0, 0), dtype=np.uint8)
# for i in range(h):
#     for j in range(w):
#         if a[i][j] != 0:
#             board[i * 100:i * 100 + 100, j * 100:j * 100 + 100] = (255, 255, 255)
#
# img = cv2.imread("./back.png")
# # print(img.shape)
# min_dim = np.min(img.shape[:2])
# max_dim = np.max(img.shape[:2])
# sub_dim = max_dim - min_dim
# img = img[sub_dim:-sub_dim, int(sub_dim / 2):-sub_dim]
# w, h, c = img.shape
# background = np.full(shape=(w * 2, h * 2, c), fill_value=(0, 0, 0), dtype=np.uint8)
# # print(background.shape)
# for i in range(2):
#     for j in range(2):
#         background[w*i:w*(i+1), h*j:h*(j+1)] = img
# print(board.shape)
# cv2.imshow("test", board)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# board = np.full(shape=[800, 800, 3], fill_value=(255, 0, 255), dtype=np.uint8)
# print(board)


# a = np.array(range(2*3*4)).reshape(2, 3, 4)
# print(a)
# # 零轴 = shape[0]
# # 1轴 = shape[1]
# b = np.sum(a, axis=0)
# print("------------")
# # 0，1，2...对应最左边的[[[...
# print(b)
# # 沿某个轴，就是将该轴压缩掉
# print(b.shape)

def board():
    l = []
    for times in range(4):
        l.append([i % 2 for i in range(8)])
        l.append([i % 2 for i in range(1, 9)])
    a = np.array(l)

    h, w = a.shape
    board = np.full(shape=[800, 800, 3], fill_value=(0, 0, 0), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if a[i][j] != 0:
                board[i * 100:i * 100 + 100, j * 100:j * 100 + 100] = (255, 255, 255)

    img = cv2.imread("back.png")
    dim = min(img.shape[0], img.shape[1])
    img = img[-dim:, :]
    img = img[::2, ::2]
    img_re = img[::-1, ::-1]
    img_left = img[::1, ::-1]
    w, h, c = img.shape
    img_b = np.zeros((w, h, c), dtype=np.uint8)
    re_img_b = copy.deepcopy(img_b)
    img_g = np.zeros((w, h, c), dtype=np.uint8)
    re_img_g = copy.deepcopy(img_g)
    img_r = np.zeros((w, h, c), dtype=np.uint8)
    re_img_r = copy.deepcopy(img_r)
    img_b[:, :, 0] = img[:, :, 1]
    img_g[:, :, 1] = img[:, :, 0]
    img_r[:, :, 2] = img[:, :, 2]
    re_img_b[:, :, :] = img_b[::-1, ::-1, :]
    re_img_g[:, :, :] = img_g[::-1, ::-1, :]
    re_img_r[:, :, :] = img_r[::-1, ::-1, :]
    list_img = [img, img_b, re_img_b, img_g, re_img_g, re_img_r, img_r, img_left, img_re]
    long = len(list_img)
    img_new = np.zeros((w * 5, h * 5, c), dtype=np.uint8)
    for i in range(5):
        for j in range(5):
            img_new[i * w:(i + 1) * w, j * h:(j + 1) * h, :] = list_img[random.randint(0, long - 1)][:, :, :]
    w1, h1, c = board.shape
    sub_w = w * 5 - w1
    sub_h = h * 5 - h1
    # img_new[int(sub_w / 2): -int(sub_w / 2), int(sub_h / 2):- int(sub_h / 2), :] = board[:, :, :]
    img_new = np.add(img_new, board)
    print(img_new.shape)
    cv2.imshow("img", img_new)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

board()

# img1 = np.zeros_like(img)
# np.stack()
# img.transpose((1, 0, 2))
# np.concatenate(img, img_b)