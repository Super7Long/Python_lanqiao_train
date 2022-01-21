"""
考虑一种简单的正则表达式：
只由 x ( ) | 组成的正则表达式。
小明想求出这个正则表达式能接受的最长字符串的长度。
例如 ((xx|xxx)x|(x|xx))xx 能接受的最长字符串是： xxxxxx，长度是 6。

输入描述:
一个由 x()| 组成的正则表达式。输入长度不超过 100，保证合法。

输出描述:
这个正则表达式能接受的最长字符串的长度。

示例:
输入
((xx\|xxx)x\|(x\|xx))xx
输出
6
"""

st = list(input())
i = 0
print(st)


def dfs():
    global i
    value = 0
    while i < len(st):
        if st[i] == '(':
            i += 1
            value += dfs()
            i += 1  # 退出一个完整括号
        elif st[i] == 'x':
            value += 1
            i += 1
        elif st[i] == '|':
            i += 1
            value = max(value, dfs())  # 返回一个括号内最大的x个数
        elif st[i] == ')':
            return value  # 直接返回值，最终返回到上一个value += dfs()
        else:
            i += 1
    return value


print(dfs())
