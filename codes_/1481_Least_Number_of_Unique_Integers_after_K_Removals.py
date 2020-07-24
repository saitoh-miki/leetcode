# %% [1481. Least Number of Unique Integers after K Removals](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/)
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = collections.Counter(arr)
        for i, j in enumerate(reversed(c.most_common())):
            if (k := k - j[1]) < 0:
                return len(c) - i
        return 0
