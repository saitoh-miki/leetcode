# %% [415. Add Strings](https://leetcode.com/problems/add-strings/)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        v, res = 0, []
        for c1, c2 in itertools.zip_longest(num1[::-1], num2[::-1]):
            n = int(c1 or 0) + int(c2 or 0) + v
            res.append(n % 10)
            v = n // 10
        if v:
            res.append(v)
        return "".join(str(c) for c in res)[::-1]
