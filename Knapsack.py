"""
题目描述：在n个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为m，每个物品的大小为A[i]
样例：
如果有4个物品[2, 3, 5, 7]
如果背包的大小为11，可以选择[2, 3, 5]装入背包，最多可以装满10的空间。
如果背包的大小为12，可以选择[2, 3, 7]装入背包，最多可以装满12的空间。
函数需要返回最多能装满的空间大小。

背包问题是计算机科学中非常经典的问题，有很多变型，但是在这里我们只是解决lintcode里的问题，更详细的内容放到以后吧。

还是通过动态规划解决，一个二维表格record记录每一步的计算结果，record[i][j] 代表前 i 个物品能否恰好填满 j 大小的空间。

拿样例来说，record[0][2] = True.

需要注意的是，record[i][j] 只是代表前 i 个物品是否“有能力”恰好填满 j 大小的空间，而不是说前 i 个物品必须全部都用上才填满

j 大小的空间。所以，不论 i 是多少，都有record[i][0] = True

那么就存在着这样的逻辑：前 i 个物品如果能恰好填满 j 大小的空间，那一定满足以下两个条件之一：

1. 不放第 i 个物品，而且前 i - 1个物品能恰好填满 j 大小的空间

2. 放第 i 个物品，而且前 i - 1个物品能恰好填满 j - A[i]大小的空间（A是物品大小的值构成的数组）

得到状态转移方程：record[i][j] = record[i - 1][j] or record[i - 1][j - A[i]]（两个条件满足一个即为真）

然后我们只需要求出满足record[i][j] = True的最大的 j 的值即可。

"""


class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backpack(m, A):
        n = len(A)
        if n == 0:
            return 0
        record = [[False for j in range(m + 1)] for i in range(n)]
        j = 0
        result = 0
        while j <= m:
            if A[0] == j:
                record[0][j] = True
                result = max(result, j)
                break
            j += 1
        record[0][0] = True

        i = 1
        while i < n:
            j = 0
            while j <= m:
                record[i][j] = record[i - 1][j] or (j - A[i] >= 0 and record[i - 1][j - A[i]])
                if record[i][j]:
                    result = max(result, j)
                j += 1
            i += 1
        return result
        # write your code here


# 一维数组
class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backpack(m, A):
        n = len(A)
        if n == 0:
            return 0
        record = [False for j in range(m + 1)]
        j = 0
        result = 0
        while j <= m:
            if A[0] == j:
                record[j] = True
                result = max(result, j)
                break
            j += 1
        record[0] = True

        i = 1
        while i < n:
            j = 0
            temp = []
            while j <= m:
                temp.append(record[j] or (j - A[i] >= 0 and record[j - A[i]]))
                if temp[j]:
                    result = max(result, j)
                j += 1
            record = temp
            i += 1
        return result

"""
题目描述：给出n个物品的体积A[i]和其价值V[i]，将他们装入一个大小为m的背包，最多能装入的总价值有多大？
样例：对于物品体积[2, 3, 5, 7]和对应的价值[1, 5, 2, 4], 假设背包大小为10的话，最大能够装入的价值为9。
"""


class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, A, V):
        n = len(A)
        if m == 0 or len(A) == 0:
            return 0
        record = [0 for j in range(m + 1)]
        j = 0
        while j <= m:
            if j >= A[0]:
                record[j] = V[0]
            j += 1

        i = 1
        result = V[0]
        while i < n:
            j = 0
            temp = []
            while j <= m:
                p = record[j - A[i]] + V[i] if j - A[i] >= 0 else 0
                temp.append(max(record[j], p))
                j += 1
            result = max(result, max(temp))
            record = temp
            i += 1
        return result
        # write your code here