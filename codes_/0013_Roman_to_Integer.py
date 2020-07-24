# %% [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        # fmt: off
        dc = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
              'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
              'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        while s:
            n = dc.get(s[:2])
            if n:
                res += n
                s = s[2:]
            else:
                res += dc[s[0]]
                s = s[1:]
        return res
