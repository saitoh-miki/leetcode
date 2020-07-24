# %% [78. Subsets](https://leetcode.com/problems/subsets/)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [sum(i, []) for i in itertools.product(*([[], [i]] for i in nums))]
