# %% [9. *Palindrome Number](https://leetcode.com/problems/palindrome-number/)
# 問題：回文かどうかを返す
# 解法：逆にして等しいか調べる
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return (s := str(x)) == s[::-1]
