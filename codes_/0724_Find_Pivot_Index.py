# %% [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)
# 問題：nums[:i] == nums[i + 1:]となるiを返せ。存在しない場合-1
# 解法：itertools.accumulateを用いる
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        for i, (n, a) in enumerate(zip(nums, itertools.accumulate(nums))):
            if a == s - a + n:
                return i
        return -1
