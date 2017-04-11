# -*- coding: utf-8 -*-
"""
题目描述：对于一个有n个数的整数数组，在对应的线段树中, 根节点所代表的区间为0-n-1, 每个节点有一个额外的属性max，
值为该节点所代表的数组区间start到end内的最大值。为SegmentTree设计一个 query 的方法，接受3个参数root, start和end，
线段树root所代表的数组中子区间[start, end]内的最大值。

样例：对于数组 [1, 4, 2, 3], 对应的线段树为：

query(root, 1, 1), return 4
query(root, 1, 2), return 4
query(root, 2, 3), return 3
query(root, 0, 2), return 4
"""


# Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None


class Solution:
    # @param root, start, end: The root of segment tree and
    #                          an segment / interval
    # @return: The maximum number in the interval [start, end]
    def query(self, root, start, end):
        if root.start > end or root.end < start or root is None:
            return
        elif root.start >= start and root.end <= end:
            return root.max
        else:
            return max(self.query(root.left, start, end), self.query(root.right, start, end))


"""
题目描述：对于一个数组，我们可以对其建立一棵 线段树, 每个结点存储一个额外的值 count 来代表这个结点所指代的数组区间内的元素个数.
 (数组中并不一定每个位置上都有元素) 实现一个 query 的方法，该方法接受三个参数 root, start 和 end, 分别代表线段树的根节点和需要
 查询的区间，找到数组中在区间[start, end]内的元素个数。
样例：
对于数组 [0, 空，2, 3], 对应的线段树为：

query(1, 1), return 0
query(1, 2), return 1
query(2, 3), return 2
query(0, 2), return 2
"""


class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None


class Solution:
    # @param root, start, end: The root of segment tree and
    #                          an segment / interval
    # @return: The count number in the interval [start, end]
    def query(self, root, start, end):
        if root is None or start > root.end or end < root.start:
            return 0
        elif start <= root.start and end >= root.end:
            return root.count
        else:
            return self.query(root.left, start, end) + self.query(root.right, start, end)