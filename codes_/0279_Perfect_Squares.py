# %% [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/)
class Solution:
    def numSquares(self, n: int) -> int:
        return numSquares(n, math.floor(math.sqrt(n)))


@functools.lru_cache(None)
def numSquares(n, m):
    if n <= 0 or not m:
        return 2 ** 31 if n else 0
    return min(numSquares(n - m * m, m) + 1, numSquares(n, m - 1))
