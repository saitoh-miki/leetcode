# %% [844. Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)
# 問題：「#」をバックスペース（1文字削除）とみなした時、SとTが等しいかを返せ
# 解法：リストをスタックとして用いる
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return calc(S) == calc(T)


def calc(s):
    res = []
    for c in s:
        if c == "#":
            if res:
                res.pop()
        else:
            res.append(c)
    return "".join(res)
