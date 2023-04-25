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
# for i in range(1, 10):
#     if i <= 5:
#         print('*' * (i * 2 - 1))
#     else:
#         print('*' * ((10 - i) * 2 - 1))
#
# # 11
# sum_num = 0
# for i in range(1, 101):
#     total = 0
#     for j in range(1, i + 1):
#         total += j
#     sum_num += total
# print(sum_num)

