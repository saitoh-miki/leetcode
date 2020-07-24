# %% [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst, c = [], [1]
        for _ in range(numRows):
            lst.append(c)
            c = [i + j for i, j in zip([0] + c, c + [0])]
        return lst
