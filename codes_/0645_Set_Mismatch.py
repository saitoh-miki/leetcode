# %% [645. Set Mismatch](https://leetcode.com/problems/set-mismatch/)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s1 = collections.Counter(range(1, len(nums) + 1))
        s2 = collections.Counter(nums)
        return [list(s2 - s1)[0], list(s1 - s2)[0]]
