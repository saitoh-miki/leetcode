# %% [290. Word Pattern](https://leetcode.com/problems/word-pattern/)


class Solution:
    def wordPattern(self, s: str, t: str) -> bool:
        return list(map(s.find, s)) == list(map((t := t.split()).index, t))

