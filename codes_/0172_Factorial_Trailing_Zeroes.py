# %% [172. *Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)
# 問題：階乗で右から0の続く数を求めよ
# 解法：5までに偶数があるので、10のN乗の個数は5のN乗の個数である
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n < 5 else n // 5 + self.trailingZeroes(n // 5)
