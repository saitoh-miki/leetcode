# %% [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i : j + 1])
