# %% [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return is_palindrome(str(x))


def is_palindrome(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n - 1 - i]:
            return False
    return True
