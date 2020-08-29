# %% [198. **House Robber](https://leetcode.com/problems/house-robber/)
# 問題：盗みを最大化せよ。連続する2軒の両方から盗んではいけない。
# 解法：各家までで、最大は「2つ前までの最大+その家」と「1つ前までの最大」のどちらか
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre = cur = 0
        for num in nums:
            pre, cur = cur, max(pre + num, cur)
        return cur
