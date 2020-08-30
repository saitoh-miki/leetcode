# %% [299. *Bulls and Cows](https://leetcode.com/problems/bulls-and-cows/)
# 問題：数当てゲームで「位置と数」が一致する個数と数のみ一致する個数を求めよ
# 解法：collections.Counterを用いる
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        co = collections.Counter
        a = sum(i == j for i, j in zip(secret, guess))
        b = sum((co(secret) & co(guess)).values()) - a
        return f"{a}A{b}B"
