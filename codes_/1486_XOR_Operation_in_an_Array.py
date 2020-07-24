# %% [1486. XOR Operation in an Array](https://leetcode.com/problems/xor-operation-in-an-array/)
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        a = [2 * i + start for i in range(n)]
        return list(itertools.accumulate(a, operator.xor))[-1]
