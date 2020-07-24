# %% [66. Plus One](https://leetcode.com/problems/plus-one/)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = "".join(str(i) for i in digits)
        return [int(c) for c in str(int(s) + 1)]
