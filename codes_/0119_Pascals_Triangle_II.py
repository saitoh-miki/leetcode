# %% [119. Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        c = [1]
        for _ in range(rowIndex):
            c = [i + j for i, j in zip([0] + c, c + [0])]
        return c
