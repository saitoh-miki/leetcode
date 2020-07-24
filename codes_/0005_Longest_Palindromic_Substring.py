# %% [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        mx = palindromic_from_center("", s, n) if n else ""
        for i in range(1, n):
            if n - i <= len(mx):
                break
            mx = palindromic_from_center(mx, s[: n - i], n - i)
            mx = palindromic_from_center(mx, s[i:], n - i)
        return mx


def palindromic_from_center(mx, s, n):
    for i in range(n // 2, -1, -1):
        if s[i] != s[n - i - 1]:
            return s[i + 1 : n - i - 1] if n - 2 * i - 2 > len(mx) else mx
    return s if n > len(mx) else mx
