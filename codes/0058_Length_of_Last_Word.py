# %% [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
