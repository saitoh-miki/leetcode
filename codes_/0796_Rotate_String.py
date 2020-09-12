# %% [796. Rotate String](https://leetcode.com/problems/rotate-string/)
# 問題：Aを回転（先頭N文字を後ろに移動）してBになるかどうかを返せ
# 解法：同じ長さで、2回繰り返したときに存在するか調べる
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A + A
        # if not A or not B:
        #     return A == B
        # f, i, n = A[0], -1, len(A)
        # while (i := B.find(f, i + 1)) >= 0:
        #     if A == B[i:] + B[:i]:
        #         return True
        # return False
