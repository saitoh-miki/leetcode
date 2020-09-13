# %% [812. Largest Triangle Area](https://leetcode.com/problems/largest-triangle-area/)
# 問題：三角形の最大面積を返せ
# 解法：https://mathwords.net/x1y2hikux2y1
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        for p, q, r in itertools.combinations(points, 3):
            x1, y1, x2, y2 = q[0] - p[0], q[1] - p[1], r[0] - p[0], r[1] - p[1]
            res = max(res, abs(x1 * y2 - x2 * y1) / 2)
        return res
