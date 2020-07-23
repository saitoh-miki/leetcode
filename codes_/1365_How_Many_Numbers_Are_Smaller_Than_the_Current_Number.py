# %% [1365. How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)
[](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst = sorted(nums)
        return [lst.index(i) for i in nums]
