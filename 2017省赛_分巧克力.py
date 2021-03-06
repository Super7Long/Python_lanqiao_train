# 儿童节那天有K位小朋友到小明家做客。小明拿出了珍藏的巧克力招待小朋友们。
# 小明一共有N块巧克力，其中第i块是Hi*Wi的方格组成的长方形。
# 为了公平起见，小明需要从这N块巧克力中切出K块巧克力分给小朋友们。切出的巧克力需要满足：
#   1.形状是正方形，边长是整数
#   2.大小相同
# 例如一块6x5的巧克力可以切出6块2x2的巧克力或者2块3x3的巧克力。
# 当然小朋友们都希望得到的巧克力尽可能大，你能帮小Hi计算出最大的边长是多少么？


n, k = map(int, input().split())
s = []
MAX = 0  # 最大边长
for i in range(n):  # [[3, 5], [6, 1], [7, 4], [3, 3]]
    s.append(list(map(int, input().split())))
    MAX = max(MAX, s[i][0], s[i][1])


# 返回一共可以分几块边长为size的巧克力
def sp(size):
    cunt = 0
    for i in s:
        a = i[0]//size
        b = i[1]//size
        cunt += a * b
    # print(cunt,' ',end='')
    return cunt


l, r = 0, MAX   # 整个区间为0-最大的边长
# 二分法，从中间处取值，直到左右区间重合为止
while l < r:
    mid = (l + r + 1) // 2  # 二分法。除2，向右取整
    if sp(mid) >= k:    # 够分，调整左区间
        l = mid
    else:               # 不够分，调整右区间
        r = mid - 1
    # print(l,r)

print(l)
