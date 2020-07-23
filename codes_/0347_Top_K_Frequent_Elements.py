# %% [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i for i, _ in collections.Counter(nums).most_common(k)]
