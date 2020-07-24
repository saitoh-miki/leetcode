# %% [204. Count Primes](https://leetcode.com/problems/count-primes/)
class Solution:
    def countPrimes(self, max_number: int) -> int:
        pr = list(range(3, max_number, 2))
        npr = len(pr)
        for i, n in enumerate(pr):
            if n:
                if n * n >= max_number:
                    break
                for j in range(i + n, npr, n):
                    pr[j] = 0
        return (max_number > 2) + sum(1 for i in pr if i)
