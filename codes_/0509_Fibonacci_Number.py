# %% [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
class Solution:
    def fib(self, N: int) -> int:
        i, j = 1, 0
        for _ in range(N):
            i, j = j + i, i
        return j
