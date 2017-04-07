# _*_coding=utf-8_*_
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code here
        candidates.sort()
        path, result = [], []
        begin = 0
        self.helper(begin, candidates, target, path, result)
        return self.set_list(result)

    def helper(self, begin, candidates, target, path, result):

        if sum(path) > target:
            return

            # 若满足条件：先复制，再将复制的结果加入结果列表
        if sum(path) == target:
            temp = path[:]
            result.append(temp)
            return

        for i in candidates[begin:]:
            path.append(i)
            # 带着半成品path继续探索：往这个半成品中添加元素，看能否成功
            self.helper(begin, candidates, target, path, result)
            # 返回上一层，自然要把这一层添加的值删去
            path.pop(-1)
            begin += 1

    def set_list(self, l):
        res = []
        for i in l:
            while i is not None:
                if l.count(i) != 1:
                    l.remove(i)
                else:
                    res.extend(i)
        return res


if __name__ == '__main__':
    print(Solution().combinationSum([1], 1))
