# %% [202. Happy Number](https://leetcode.com/problems/happy-number/)

class Solution:
    def isHappy(self, n: int) -> bool:
        st = {1}
        while n not in st:
            st.add(n)
            n, s = 0, str(n)
            n = sum(int(c)**2 for c in s)
        return n == 1
