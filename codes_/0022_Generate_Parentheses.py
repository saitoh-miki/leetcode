# %% [22. **Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
# 問題：有効な「n個の括弧からなる文字」を列挙
# 解法：左括弧と右括弧について再帰
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return list(search("(" * n, "", ""))


def search(left, right, cur):
    if left:
        yield from search(left[:-1], right + left[-1], cur + left[-1])
    if right:
        yield from search(left, right[:-1], cur + chr(81 - ord(right[-1])))
    elif not left:
        yield cur
