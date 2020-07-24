# %% [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        n = len(p)
        dc = collections.Counter(p)
        dc -= collections.Counter(c for c in s[: n - 1] if c in p)
        for i in range(n - 1, len(s)):
            if i >= n and s[i - n] in p:
                dc[s[i - n]] += 1
            if s[i] in p:
                dc[s[i]] -= 1
            if not any(dc.values()):
                res.append(i - n + 1)
        return res
