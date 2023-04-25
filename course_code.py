import copy
import random
from filecmp import cmp
import os

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
#         print(f"姓名：{card['name']}\t年龄:{card['age']}\t性别:{card['sex']}\ttel:{card['tel']}\taddr:{card['addr']}")
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
#         for m in range(2, month + 1):
#             num_temp = 0
#             num_temp += num[m - 1] + num[m - 2]
#             num.append(num_temp)
#             print(num)
#     return num[-1]
#
#
# print(count(10))






