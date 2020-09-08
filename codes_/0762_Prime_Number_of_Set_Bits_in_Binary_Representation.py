# %% [762. Prime Number of Set Bits in Binary Representation](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/)
# 問題：[L, R]の範囲で条件を満たす数字の個数を返せ。条件は2進数で1になる数が素数であること
# 解法：Rは1000_000以下であり、2進数で22ビット以下となり、素数は2, 3, 5, 7, 11, 13, 17, 19しかない
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        st = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(i).count("1") in st for i in range(L, R + 1))
