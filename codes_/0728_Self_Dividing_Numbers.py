# %% [728. Self Dividing Numbers](https://leetcode.com/problems/self-dividing-numbers/)
# 問題：leftからrightまででself-dividingの数をリストで返せ。self-dividingは、各桁の数字で割り切れる
# 解法：各桁は`k, m = m % 10, m // 10`のように更新する
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [n for n in range(left, right + 1) if ok(n)]


def ok(n):
    m = n
    while m:
        k, m = m % 10, m // 10
        if not k or n % k:
            return False
    return True
