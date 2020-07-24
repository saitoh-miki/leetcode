# %% [633. Sum of Square Numbers](https://leetcode.com/problems/sum-of-square-numbers/)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        st, n = set(), round(c ** 0.5)
        for i, num in enumerate(i * i for i in range(n + 1)):
            if num in st or num == c or 2 * num == c:
                return True
            st.add(c - num)
        return False
