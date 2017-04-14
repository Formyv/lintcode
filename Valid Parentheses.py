"""
题目描述：给定一个字符串所表示的括号序列，包含以下字符： '(', ')', '{', '}', '[' and ']'， 判定是否是有效的括号序列。

样例：括号必须依照 "()" 顺序表示， "()[]{}" 是有效的括号，但 "([)]"则是无效的括号。
"""

#
# class Solution:
#     # @param {string} s A string
#     # @return {boolean} whether the string is a valid parentheses
#     def isValidParentheses(self, s):
#         # Write your code here
#         left = ['(', '[', '{']
#         right = [')', ']', '}']
#         stack = []
#         if len(s) % 2 == 1:
#             return False
#         for i in s:
#             if i in left:
#                 stack.append(i)
#             elif not stack and i in right:
#                 return False
#             elif left.index(stack.pop()) != right.index(i):
#                 return False
#         if len(stack) == 0:
#             return True
#         else:
#             return False


class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        table = {"(": ")", "[": "]", "{": "}"}
        n = len(s)
        stack = []
        for i in s:
            if len(stack) > 0 and stack[-1] in table and table[stack[-1]] == i:
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0


if __name__ == '__main__':
    print(Solution().isValidParentheses("}}{{"))