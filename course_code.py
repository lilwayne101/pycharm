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
# chr() ASC||表类型转换
# complex() 复数的类型转换
# round() 四舍五入的内置函数

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
#     print(a / b)
# if c == '//':
#     print(a // b)
# if c == '%':
#     print(a % b)
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



