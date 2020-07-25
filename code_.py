# %% [414. Third Maximum Number](https://leetcode.com/problems/third-maximum-number/)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = sorted(set(nums), reverse=True)
        return s[0] if len(s) < 3 else s[2]


# %%
Solution().thirdMax([2, 2, 3, 1, 4])


# %%
