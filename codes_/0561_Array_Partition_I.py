# %% [561. Array Partition I](https://leetcode.com/problems/array-partition-i/)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(i for i in sorted(nums)[::2])
