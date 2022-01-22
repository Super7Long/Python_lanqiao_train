"""
有 n 辆自行车依次来到停车棚，除了第一辆自行车外，每辆自行车都会恰好停放在已经在停车棚里的某辆自行车的左边或右边。
(e.g.停车棚里已经有 3 辆自行车，从左到右编号为：3,5,1现在编号为 2 的第 4 辆自行车要停在 5 号自行车的左边，所以现在停车棚里的自行车编号是：3,2,5,1)。
给定nn辆自行车的停放情况，按顺序输出最后停车棚里的自行车编号。n≤100000。

输入描述
第一行一个整数 n。 第二行一个整数x。表示第一辆自行车的编号。 以下 n-1 行，每行 3 个整数 x,y,z。 z=0时，表示编号为 x 的自行车恰停放在编号为 y 的自行车的左边。
z=1 时，表示编号为 x 的自行车恰停放在编号为 y 的自行车的右边。

输出描述
从左到右输出停车棚里的自行车编号

示例
输入
4
3
1 3 1
2 1 0
5 2 1

输出
3 2 5 1
"""
N = int(input())


# 创建双向链表的节点类
class Lbnode(object):
    def __init__(self, data):
        self.data = data
        self.pre = None
        self.next = None
# 创建字典，便于找到每个数据对应的位置（便于插入，删除）


numloca = {}
h = int(input())
node = Lbnode(h)  # 链表中头节点地址
head = node
# print(node)
numloca[h] = node  # 向字典中添加头节点信息（键：自行车编号(h) 值：编号地址(node)）
# 插入N - 1个节点（剩余节点）
for i in range(N - 1):
    x, y, z = map(int, input().split())
    node = Lbnode(x)  # 自行车编号x的节点地址
    # 当z = 1时，x插入y的右边
    if z == 1:
        # 判断y右边是否为空(next)，不为空则将插入节点与后面的节点连接
        if numloca[y].next:
            # 进行节点连接（1. y与插入数据进行连接 2. y右边的数据与插入数据连接  1+2. 插入数据与其左右两边数据连接）
            numloca[y].next.pre = node # 把y右边节点的前一个节点地址赋值为x的节点地址
            node.next = numloca[y].next
        # 进行插入（x插入y的右边）
        numloca[y].next = node  # 把x的地址插入y的右边
        node.pre = numloca[y]
    # z = 0，x插入y的左边
    else:
        # 判断y左边是否为空(pre)，不为空则将插入节点与前面的节点连接，为空则插入后标注为头节点
        if not numloca[y].pre:  # 等价于 if numloca[y].pre == None:
            # 进行节点连接
            numloca[y].pre = node  # 把y节点的前一个节点地址赋值为x的节点地址
            node.next = numloca[y]
            # 进行插入（x插入y的左边）
            head = node  # x为头节点
        else:  # 不为空
            # 连接进行（1. y与插入数据进行连接 2. y左边的数据与插入数据连接  1+2. 插入数据与其左右两边数据连接）
            numloca[y].pre.next = node  # 把y节点的前一个节点的下个节点地址赋值为x的节点地址
            node.pre = numloca[y].pre
            # 进行插入（x插入y的左边）
            numloca[y].pre = node
            node.next = numloca[y]
    # 记录x的位置(向字典中添加头节点信息（键：自行车编号(x) 值：编号地址(node)）)
    numloca[x] = node

# 打印输出
while head:  # 链表已经保存完毕（自行车已经停放完了），从头节点开始进行输出，当取完之后跳出循环
    print(head.data, end=' ')
    head = head.next  # 下一个节点的地址
