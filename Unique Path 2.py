# _*_coding=utf-8_*_
class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        if m == 0 or obstacleGrid[0][0] == 1:
            return 0
        n = len(obstacleGrid[0])
        record = [[1 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    record[i][j] = 0
                elif j == 0:
                    record[i][j] = record[i - 1][j]
                elif i == 0:
                    record[i][j] = record[i][j - 1]
                else:
                    record[i][j] = record[i - 1][j] + record[i][j - 1]
        return record[m - 1][n - 1]
        # write your code here

