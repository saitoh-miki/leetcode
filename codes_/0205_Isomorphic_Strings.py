# %% [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dc1, dc2 = {}, {}
        for i, (c, d) in enumerate(zip(s, t)):
            if dc1.get(c, -1) != dc2.get(d, -1):
                return False
            dc1[c] = dc2[d] = i
        return True
