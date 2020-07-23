# %% [1221. Split a String in Balanced Strings](https://leetcode.com/problems/split-a-string-in-balanced-strings/)

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = cnt = 0
        for c in s:
            cnt += (c == 'L') * 2 - 1
            res += not cnt
        return res
