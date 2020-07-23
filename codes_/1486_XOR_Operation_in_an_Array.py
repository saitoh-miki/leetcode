# %% [1486. XOR Operation in an Array](https://leetcode.com/problems/xor-operation-in-an-array/)

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return list(itertools.accumulate(
            [2 * i + start for i in range(n)], operator.xor))[-1]
