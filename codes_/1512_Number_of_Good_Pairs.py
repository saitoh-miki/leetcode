# %% [1512. Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/)

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(n * (n - 1) // 2 for n in collections.Counter(nums).values())


