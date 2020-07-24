# %% [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lst = [i for i in nums if i]
        nums[:] = lst + [0] * (len(nums) - len(lst))
