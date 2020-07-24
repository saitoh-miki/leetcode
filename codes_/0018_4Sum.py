# %% [18. 4Sum](https://leetcode.com/problems/4sum/)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res, n = [], len(nums)
            if n and (nums[0] <= target / k <= nums[-1]):
                if k == 2:
                    return twoSum(nums, target)
                for i in range(n):
                    if i == 0 or nums[i - 1] != nums[i]:
                        for st in kSum(nums[i + 1 :], target - nums[i], k - 1):
                            res.append([nums[i]] + st)
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res, n = [], len(nums)
            lo, hi = 0, n - 1
            while lo < hi:
                sum = nums[lo] + nums[hi]
                if sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif sum > target or (hi < n - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res

        nums.sort()
        return kSum(nums, target, 4)
