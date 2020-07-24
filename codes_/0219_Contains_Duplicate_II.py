# %% [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}
        for i, num in enumerate(nums, k + 1):
            if i - pos.get(num, 0) <= k:
                return True
            pos[num] = i
        return False
