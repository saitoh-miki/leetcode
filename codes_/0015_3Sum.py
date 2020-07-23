# %% [15. 3Sum](https://leetcode.com/problems/3sum/)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        ct = collections.Counter(nums)
        for k, v in ct.items():
            if not k:
                if v > 2:
                    res.append((0, 0, 0))
            else:
                if v > 1 and ct[-2 * k]:
                    res.append(tuple(sorted([k, k, -2 * k])))
                for ts in twosum(ct, -k):
                    res.append(tuple(sorted([k, *ts])))
        return set(res)

def twosum(c, t):
    for i, v in c.items():
        w = c[t - i]
        if  2 * i < t and w:
            if (i != -t or v > 1) and (2 * t != i or w > 1):
                yield i, t - i
