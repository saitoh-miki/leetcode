# %% [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        pali = lambda t: t == t[::-1]
        for i in range((n := len(s)) // 2):
            j = n - 1 - i
            if s[i] != s[j]:
                return pali(s[i:j]) or pali(s[i + 1 : j + 1])
        return True
