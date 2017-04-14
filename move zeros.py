"""
题目描述：给一个数组 nums 写一个函数将 0 移动到数组的最后面，非零元素保持原数组的顺序

样例：给出 nums = [0, 1, 0, 3, 12], 调用函数之后, nums = [1, 3, 12, 0, 0].
"""


class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place
    def moveZeroes(self, nums):
        add = [0] * nums.count(0)
        cur = list(filter(lambda x: x != 0, nums))
        return cur+add

if __name__ == '__main__':
    print(Solution().moveZeroes([0, 1, 0, 2, 4, 3]))