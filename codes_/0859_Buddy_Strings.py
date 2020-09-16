# %% [859. Buddy Strings](https://leetcode.com/problems/buddy-strings/)
# 問題：Aから2文字をswapしてBにできるかを返せ
# 解法：例題をカバーする
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if not (n := len(A)) or n != len(B):
            return False
        if A == B:
            return collections.Counter(A).most_common()[0][1] > 1
        res = []
        for a, b in zip(A, B):
            if a != b:
                res.append((a, b))
        return len(res) == 2 and res[0] == res[1][::-1]
