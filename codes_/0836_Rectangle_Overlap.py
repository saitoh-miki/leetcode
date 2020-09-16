# %% [836. *Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/)
# 問題：2つの長方形が重なるかどうかを返せ
# 解法：X軸、Y軸で重なるかを調べる
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2, x3, y3, x4, y4 = *rec1, *rec2
        return x1 < x4 and x3 < x2 and y1 < y4 and y3 < y2
