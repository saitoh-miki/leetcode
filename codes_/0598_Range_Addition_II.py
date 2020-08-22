# %% [598. Range Addition II](https://leetcode.com/problems/range-addition-ii/)
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return min(i for i, j in ops) * min(j for i, j in ops) if ops else m * n
