# %% [665. Non-decreasing Array](https://leetcode.com/problems/non-decreasing-array/solution/)
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        p = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if p is not None:
                    return False
                p = i
        return (
            p in (None, 0, len(nums) - 2)
            or nums[p - 1] <= nums[p + 1]
            or nums[p] <= nums[p + 2]
        )
