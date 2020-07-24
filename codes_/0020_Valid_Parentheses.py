# %% [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
class Solution:
    def isValid(self, s: str) -> bool:
        lst, dc = [], dict(zip("({[", ")}]"))
        for c in s:
            if c in "({[":
                lst.append(dc[c])
            elif not lst or c != lst.pop():
                return False
        return not lst
