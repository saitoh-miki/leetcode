# %% [657. Robot Return to Origin](https://leetcode.com/problems/robot-return-to-origin/)
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c = collections.Counter(moves)
        return c.get("L", 0) == c.get("R", 0) and c.get("D", 0) == c.get("U", 0)
