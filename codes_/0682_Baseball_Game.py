# %% [682. Baseball Game](https://leetcode.com/problems/baseball-game/)
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for op in ops:
            if op == "+":
                res.append(res[-2] + res[-1])
            elif op == "D":
                res.append(res[-1] * 2)
            elif op == "C":
                res.pop()
            else:
                res.append(int(op))
        return sum(res)
