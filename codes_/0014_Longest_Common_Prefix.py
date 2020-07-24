# %% [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for cc in zip(*strs):
            if not all(cc[0] == c for c in cc[1:]):
                break
            res.append(cc[0])
        return "".join(res)
