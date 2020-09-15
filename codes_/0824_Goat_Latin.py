# %% [824. Goat Latin](https://leetcode.com/problems/goat-latin/)
class Solution:
    def toGoatLatin(self, S: str) -> str:
        return " ".join(func(*i) for i in enumerate(S.split()))


def func(i, s):
    t = s if s[0] in "aeiouAEIOU" else s[1:] + s[0]
    return t + "maa" + "a" * i
