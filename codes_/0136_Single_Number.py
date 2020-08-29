# %% [136. *Single Number](https://leetcode.com/problems/single-number/)
# 問題：1つしか存在しない数を求めよ
# 解法：XORで累積する
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res
