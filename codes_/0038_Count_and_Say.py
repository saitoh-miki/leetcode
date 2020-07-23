# %% [38. Count and Say](https://leetcode.com/problems/count-and-say/)

class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            s = ''.join(f'{len(list(g[1]))}{g[0]}' for g in itertools.groupby(s))
        return s
