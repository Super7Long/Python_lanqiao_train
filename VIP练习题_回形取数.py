"""
回形取数就是沿矩阵的边取数，若当前方向上无数可取或已经取过，则左转90度。一开始位于矩阵左上角，方向向下。

输入描述:
输入第一行是两个不超过 200 的正整数 m, n，表示矩阵的行和列。接下来 m 行每行 n 个整数，表示这个矩阵。

输出描述
输出只有一行，共 m*n 个数，为输入矩阵回形取数得到的结果。数之间用一个空格分隔，行末不要有多余的空格。

示例:
输入
3 3
1 2 3
4 5 6
7 8 9

输出
1 4 7 8 9 6 3 2 5
"""
hl = input().split()
lb = []
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 四个方向，进行旋转
value = []  # 把结果保存在列表里

# 回型取数的数据
for i in range(int(hl[0])):
    h = input().split()
    lb.append(h)
# print(lb)
x, y = -1, 0  # 刚开始进行取数的坐标
d = 0  # 取四个方向的坐标值
flag = 0  # 统计结果列表的个数
for j in range(int(hl[0]) * int(hl[1])):
    nx, ny = x + dir[d][0], y + dir[d][1]
    if nx < 0 or nx >= int(hl[0]) or ny < 0 or ny >= int(hl[1]) or lb[nx][ny] == -1:  # 判断是否超出边界 or 该值已经取过
        d = (d + 1) % 4  # 四个方向的坐标取值计算
        x, y = x + dir[d][0], y + dir[d][1]  # 进行旋转，继续取值
    else:
        x, y = nx, ny
    value.append(lb[x][y])
    # print(lb[x][y], end=' ')
    lb[x][y] = -1  # 已经取过的值赋予-1，防止继续取

# 题目要求行末不要有多余的空格，因此进行以下操作
for k in value:
    flag += 1
    if flag == len(value):
        print(k, end='')
    else:
        print(k, end=' ')
