# %% [406. Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/)

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        dic = collections.defaultdict(list)
        for i, (h, k) in enumerate(people):
            dic[h].append((k, i))
        height = set(h for h, _ in people)
        for h in sorted(height, reverse=True):
            for pos, idx in sorted(dic[h]):
                res.insert(pos, people[idx])
        return res
