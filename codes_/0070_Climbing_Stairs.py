# %% [70. *Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
# 問題：1段または2段ずつ登れる階段で、異なる登り方の種類数を求めよ
# 解法：n段ならフィボナッチ数F_{n+1}を求めれば良い。see 500
class Solution:
    def climbStairs(self, n: int) -> int:
        val, nxt = 1, 1
        for _ in range(n - 1):
            val, nxt = nxt, val + nxt
        return nxt
