# %% [581. Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/)

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        lst = sorted(nums)
        s = same_len(lst, nums)
        e = same_len(reversed(lst), reversed(nums))
        return max(0, len(nums) - e - s)

def same_len(lst1, lst2):
    for i, (j, k) in enumerate(zip(lst1, lst2)):
        if j != k:
            return i
    return len(list(lst1))
