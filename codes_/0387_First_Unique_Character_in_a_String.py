# %% [387. *First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for k, v in collections.Counter(s).items():
            if v == 1:
                return s.index(k)
        return -1
