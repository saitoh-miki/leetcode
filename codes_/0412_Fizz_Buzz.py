# %% [412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = range(1, n + 1)
        return [("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)) or str(i) for i in a]
