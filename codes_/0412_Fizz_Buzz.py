# %% [412. *Fizz Buzz](https://leetcode.com/problems/fizz-buzz/)
# 問題：n以下のFizz Buzzを求めよ。https://ja.wikipedia.org/wiki/Fizz_Buzz
# 解法：「文字列*条件」と「or」も用いる
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = range(1, n + 1)
        return [("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)) or str(i) for i in a]
