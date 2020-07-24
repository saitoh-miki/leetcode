# %% [278. First Bad Version](https://leetcode.com/problems/first-bad-version/)
class Solution:
    def firstBadVersion(self, n):
        lo, up = 0, n
        while up - lo > 1:
            mid = (lo + up) // 2
            if isBadVersion(mid):
                up = mid
            else:
                lo = mid
        return up
