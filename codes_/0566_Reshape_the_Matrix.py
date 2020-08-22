# %% [566. Reshape the Matrix](https://leetcode.com/problems/reshape-the-matrix/)
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(nums) * len(nums[0]):
            return nums
        it = itertools.chain(*nums)
        return [[next(it) for _ in range(c)] for _ in range(r)]
