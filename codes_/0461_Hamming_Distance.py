# %% [461. Hamming Distance](https://leetcode.com/problems/hamming-distance/)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(i != j for i, j in zip(bin(x)[2:].zfill(31), bin(y)[2:].zfill(31)))
