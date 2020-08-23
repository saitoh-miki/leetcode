# %% [16. **3Sum Closest](https://leetcode.com/problems/3sum-closest/)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n, diff = len(nums), math.inf
        nums.sort()
        for i in range(n):
            lo, hi = i + 1, n - 1
            while lo < hi:
                sm = nums[i] + nums[lo] + nums[hi]
                if abs(target - sm) < abs(diff):
                    diff = target - sm
                if sm < target:
                    lo += 1
                else:
                    hi -= 1
            if not diff:
                break
        return target - diff
