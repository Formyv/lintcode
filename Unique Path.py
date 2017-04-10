# _*_coding=utf-8_*_
# method_1
# DP
class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """

    def uniquePaths(self, m, n):
        if m < 1 or n < 1:
            return 0
            # 方便起见，令表格初始化为全部是1
        record = [[1 for i in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                record[i][j] = record[i - 1][j] + record[i][j - 1]
        return record[m - 1][n - 1]
        # write your code here


# method_2
# recursion
class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """

    def uniquePaths(self, m, n):
        if m < 1 or n < 1:
            return 0
        if m == 1 and n == 1:
            return 1
        else:
            return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
            # write your code here