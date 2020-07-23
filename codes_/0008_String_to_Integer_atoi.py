# %% [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

class Solution:
    def myAtoi(self, s: str) -> int:
        try:
            s = re.match(r'\+?-?[0-9]+', s.strip()).group()
            return min(2147483647, max(-2147483648, int(s)))
        except:
            return 0
