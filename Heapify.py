"""
题目描述：给出一个整数数组，堆化操作就是把它变成一个最小堆数组。对于堆数组A，A[0]是堆的根，
并对于每个A[i]，A [i * 2 + 1]是A[i]的左儿子并且A[i * 2 + 2]是A[i]的右儿子。
样例：给出 [3,2,1,4,5]，返回[1,2,3,4,5] 或者任何一个合法的堆数组
"""
class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        for i in A:
            cur = i
            par = (i - 1) // 2
            while par >= 0 and A[par] > A[cur]:
                A[par], A[cur] = A[cur], A[par]
                cur = par
                par = (cur-1)//2

"""
heap:
    class Heap(object):
        def __init__(self, elements):
            self.vector = []
            for element in elements:
                self.add(element)

        def add(self, element):

            # 添加新元素到列表末尾
            self.vector.append(element)

            # 找到新添加节点的父亲
            cur = len(self.vector) - 1
            par = (cur - 1) // 2

            # 逐层交换
            while cur != 0 and self.vector[cur] > self.vector[par]:
                self.vector[par], self.vector[cur] = self.vector[cur], self.vector[par]
                cur = par
                par = (cur - 1) // 2

        def pop(self):

            # Next决定是否还需要进行下一步交换
            Next = True

            # 首尾交换
            self.vector[0], self.vector[-1] = self.vector[-1], self.vector[0]

            # 将尾元素（其实是根节点）删除出来
            result = self.vector.pop()

            cur = 0

            # 我们认为只要这一步进行交换了，且还能交换（当前节点还有孩子），就继续交换
            while cur < len(self.vector) and Next:
                Next = False

                # 找左右孩子的索引
                left_child, right_child = (2 * cur) + 1, (2 * cur) + 2

                # 左孩子索引越界，交换终止
                if left_child >= len(self.vector):
                    break

                # 右孩子存在
                if right_child < len(self.vector):

                    # max_index：较大孩子的索引
                    max_index = right_child if self.vector[left_child] < self.vector[right_child] else left_child
                    if self.vector[cur] < self.vector[max_index]:
                        self.vector[cur], self.vector[max_index] = self.vector[max_index], self.vector[cur]
                        cur = max_index
                        Next = True

                # 右孩子不存在
                elif self.vector[cur] < self.vector[left_child]:
                    self.vector[cur], self.vector[left_child] = self.vector[left_child], self.vector[cur]
                    cur = left_child
                    Next = True

            # 返回被删除的值
            return result

"""