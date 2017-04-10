class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None


class Solution:
    # @oaram A: a list of integer
    # @return: The root of Segment Tree
    def build(self, A):
        start, end = 0, len(A) - 1
        if start > end:
            return
        return self.helper(A, start, end)

    def helper(self, A, start, end):
        if start == end:
            return SegmentTreeNode(start, end, A[start])
        root = SegmentTreeNode(start, end, max(A[start: end + 1]))
        mid = (start + end) // 2
        root.left = self.helper(A, start, mid)
        root.right = self.helper(A, mid + 1, end)
        return root
        # write your code here