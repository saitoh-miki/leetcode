# %% [1. *Two Sum](https://leetcode.com/problems/two-sum/)
# 問題：numsから、和がtargetになる2つの数字を取り出し、インデックスを返す
# 解法：各数字numに対しtarget - numがキー、インデックスが値となるよう覚える
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dc = {}
        for i, num in enumerate(nums):
            if num in dc:
                return [dc[num], i]
            dc[target - num] = i
