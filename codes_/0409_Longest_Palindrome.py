# %% [409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = collections.Counter(s).values()
        f = any(i % 2 for i in c)
        return sum(i & 0xFFFFFFFE for i in c) + f
