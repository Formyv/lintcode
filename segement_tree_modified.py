"""
题目描述：对于一棵 最大线段树, 每个节点包含一个额外的 max 属性，用于存储该节点所代表区间的最大值。
设计一个 modify 的方法，接受三个参数 root、 index 和 value。该方法将 root 为跟的线段树中 [start, end] =
[index, index] 的节点修改为了新的 value ，并确保在修改后，线段树的每个节点的 max 属性仍然具有正确的值。
"""


class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None


class Solution:
    """
    @param root, index, value: The root of segment tree and
    @ change the node's value with [index, index] to the new given value
    @return: nothing
    """

    def modify(self, root, index, value):
        # 查询与节点没有交集，剪枝
        if root is None or root.start > index or root.end < index:
            return
            # 搜索到叶子节点，修改
        elif root.end == root.start == index:
            root.max = value
            # 递归的过程
        else:
            self.modify(root.left, index, value)
            self.modify(root.right, index, value)
            root.max = max(root.left.max, root.right.max)
            # write your code here