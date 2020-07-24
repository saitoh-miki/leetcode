# %% [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        lf, ri = 0, len(height) - 1
        while lf < ri:
            maxarea = max(maxarea, min(height[lf], height[ri]) * (ri - lf))
            if height[lf] < height[ri]:
                lf += 1
            else:
                ri -= 1
        return maxarea
