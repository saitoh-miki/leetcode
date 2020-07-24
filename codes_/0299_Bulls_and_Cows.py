# %% [299. Bulls and Cows](https://leetcode.com/problems/bulls-and-cows/)

co = collections.Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = sum(i == j for i, j in zip(secret, guess))
        b = sum((co(secret) & co(guess)).values()) - a
        return f"{a}A{b}B"

