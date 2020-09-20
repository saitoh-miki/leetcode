# %% [169. *Majority Element](https://leetcode.com/problems/majority-element/)
# 問題：最頻値を求めよ
# 解法：collections.Counterを使え
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]
