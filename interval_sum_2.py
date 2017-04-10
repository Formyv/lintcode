# time limit exceeded
class Solution:
    # @param A: An integer list
    def __init__(self, A):
        # write your code here
        self.l = A

    # @param start, end: Indices
    # @return: The sum from start to end
    def query(self, start, end):
        # write your code here
        if start < 0 or end > len(self.l) or start > end:
            return 0
        s = 0
        for i in range(start, end+1):
            s += self.l[i]
        return s

    # @param index, value: modify A[index] to value.
    def modify(self, index, value):
        # write your code here
        self.l[index] = value

# segement tree


if __name__ == '__main__':
    print(Solution([1, 2, 7, 8, 5]).query(0, 2))
