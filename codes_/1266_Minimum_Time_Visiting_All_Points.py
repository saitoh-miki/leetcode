# %% [1266. Minimum Time Visiting All Points](https://leetcode.com/problems/minimum-time-visiting-all-points/)
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(
            max(abs(pt2[0] - pt1[0]), abs(pt2[1] - pt1[1]))
            for pt1, pt2 in zip(points, points[1:])
        )
