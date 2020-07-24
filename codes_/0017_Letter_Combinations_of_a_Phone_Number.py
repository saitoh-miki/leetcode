# %% [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
letters = "_ _ abc def ghi jkl mno pqrs tuv wxyz".split()


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        return map("".join, itertools.product(*(letters[int(c)] for c in digits)))
