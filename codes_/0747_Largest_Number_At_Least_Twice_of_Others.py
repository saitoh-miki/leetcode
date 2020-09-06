# %% [747. Largest Number At Least Twice of Others](https://leetcode.com/problems/largest-number-at-least-twice-of-others/)
# 問題：ただ1つ存在する最大値のインデックスを返せ。ただし、その最大値が2番目に大きい値の2倍未満なら-1を返せ
# 解法：最初に最大値を求め、すべての数字をチェックする
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        mx = max(nums)
        if all(mx >= 2 * num for num in nums if num != mx):
            return nums.index(mx)
        return -1
