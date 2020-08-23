# %% [22. **Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
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
