# %% [17. *Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
# 問題：数字の文字列から、可能性のある文字の組み合わせを返す
# 解法：全列挙
letters = "_ _ abc def ghi jkl mno pqrs tuv wxyz".split()


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        return map("".join, itertools.product(*(letters[int(c)] for c in digits)))
