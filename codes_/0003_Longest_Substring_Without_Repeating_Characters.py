# %% [3. *Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, i, n, idx = 0, 0, len(s), {}
        for j, c in enumerate(s):
            i = max(i, idx.get(c, 0))
            res = max(res, j - i + 1)
            idx[c] = j + 1
        return res
