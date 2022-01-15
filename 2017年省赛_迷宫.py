"""
房间的地板上写着一个很大的字母。我们假设玩家是面朝上坡的方向站立，则：
L表示走到左边的房间，
R表示走到右边的房间，
U表示走到上坡方向的房间，
D表示走到下坡方向的房间。
X 星球的居民有点懒，不愿意费力思考。他们更喜欢玩运气类的游戏。这个游戏也是如此！
开始的时候，直升机把100名玩家放入一个个小房间内。玩家一定要按照地上的字母移动。
迷宫地图如下：
UDDLUULRUL
UURLLLRRRU
RRUURLDLRD
RUDDDDUUUU
URUDLLRRUU
DURLRLDLRL
ULLURLLRDU
RDLULLRDDD
UUDDUDUDLL
ULRDLUURRR
请你计算一下，最后，有多少玩家会走出迷宫，而不是在里边兜圈子？
"""

import copy  # 使用拷贝函数
str = ['UDDLUULRUL',
       'UURLLLRRRU',
       'RRUURLDLRD',
       'RUDDDDUUUU',
       'URUDLLRRUU',
       'DURLRLDLRL',
       'ULLURLLRDU',
       'RDLULLRDDD',
       'UUDDUDUDLL',
       'ULRDLUURRR']
str1 = []
s = []
# print(str)

# 把迷宫保存在一个二维列表里，形成一个坐标系
for i in range(len(str)):
    str1.append(list(str[i]))
    s.append(list(str[i]))
# print(str1)
# print(s)
# print(len(str1), len(str1[0]))
step = 0  # 统计可以走出迷宫的人数

# 把迷宫的最左上角设定为坐标原点(x, y)=(0, 0) 横坐标表示y轴 纵坐标表示x轴
for j in range(len(str1)):  # 坐标x
    for k in range(len(str1[0])):  # 坐标y
        x, y = j, k
        str1 = copy.deepcopy(s)  # 要使用深拷贝，把列表中修改的-1值还原（直接赋值是浅拷贝）
        # print('s:', s)
        # print('str1:', str1)
        while True:  # 利用死循环，当出现无法走出迷宫 or 成功走出时才退出改死循环
            if str1[x][y] == 'U':
                str1[x][y] = -1
                x -= 1
                if x < 0:
                    # print(x, y)
                    step += 1
                    break
            if str1[x][y] == 'D':
                str1[x][y] = -1
                x += 1
                if x > (len(str1) - 1):
                    # print(x, y)
                    step += 1
                    break
            if str1[x][y] == 'L':
                str1[x][y] = -1
                y -= 1
                if y < 0:
                    # print(x, y)
                    step += 1
                    break
            if str1[x][y] == 'R':
                str1[x][y] = -1
                y += 1
                if y > (len(str1[0]) - 1):
                    # print(x, y)
                    step += 1
                    break
            if str1[x][y] == -1:
                break
print(step)  # 打印从迷宫出来的总人数

