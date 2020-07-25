# %% [443. String Compression](https://leetcode.com/problems/string-compression/)
class Solution:
    def compress(self, chars: List[str]) -> int:
        p, n, a = chars[0], 0, []
        for c in chars + [""]:
            if c == p:
                n += 1
            elif n:
                a.extend(f"{p}{n if n - 1 else ''}")
                p, n = c, 1
        chars[:] = a
        return len(a)
