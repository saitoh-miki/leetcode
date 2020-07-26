# %% [459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return re.match(r"(.+)\1+$", s)
