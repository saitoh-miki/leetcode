# %% [6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lst = [[] for _ in range(numRows)]
        for cc in use(s, numRows):
            for i, c in enumerate(cc):
                lst[i].append(c)
        return ''.join(''.join(i) for i in lst)

def use(s, numRows):
    p, n = 0, len(s)
    while p < n:
        yield [s[p + i] if p + i < n else '' for i in range(numRows)]
        p += numRows
        for i in range(1, numRows - 1):
            if p < n:
                yield [''] * (numRows - i - 1) + [s[p]] + [''] * i
                p += 1
