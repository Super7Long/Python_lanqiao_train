"""
给定数列 1, 1, 1, 3, 5, 9, 17, ⋯，从第 4 项开始，每项都是前 3 项的和。
求第 20190324 项的最后 4 位数字。
"""
num1, num2, num3 = 1, 1, 1
lb = [1, 1, 1]
while True:
    a, b, c = num1, num2, num3
    num1 = b
    num2 = c
    num3 = (a + b + c) % 10000  # 保存数的最后4位，也防止数据溢出。
    lb.append(num3)
    if len(lb) == 20190324:  # 第20190324项的数字
        break
print(num3)
