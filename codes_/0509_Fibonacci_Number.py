# %% [509. *Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
# 問題：フィボナッチ数を求めよ
# 解法：`val, nxt = 0, 1`で初期化し`val, nxt = nxt, val + nxt`で更新する
class Solution:
    def fib(self, N: int) -> int:
        val, nxt = 0, 1
        for _ in range(N):
            val, nxt = nxt, val + nxt
        return val
