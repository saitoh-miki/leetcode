# %% [20. *Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
# 問題：括弧が有効かどうかを返す
# 解法：1文字ずつ括弧開きをスタックに積む。括弧閉じが対応しているかを調べる
class Solution:
    def isValid(self, s: str) -> bool:
        lst, dc = [], dict(zip("({[", ")}]"))
        for c in s:
            if c in "({[":
                lst.append(dc[c])
            elif not lst or c != lst.pop():
                return False
        return not lst
