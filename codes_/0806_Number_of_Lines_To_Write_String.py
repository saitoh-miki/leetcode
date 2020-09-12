# %% [806. Number of Lines To Write String](https://leetcode.com/problems/number-of-lines-to-write-string/)
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        lines, cur = 1, 0
        dc = {chr(97 + i): n for i, n in enumerate(widths)}
        for c in S:
            n = dc[c]
            if (cur := cur + n) > 100:
                lines += 1
                cur = n
        return [lines, cur]
