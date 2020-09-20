# %% [347. *Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
# 問題：上位K個の高頻度の要素を返せ
# 解法：collections.Counterを用いる
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i for i, _ in collections.Counter(nums).most_common(k)]
