# %% [389. *Find the Difference](https://leetcode.com/problems/find-the-difference/)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list((collections.Counter(t) - collections.Counter(s)).keys())[0]
