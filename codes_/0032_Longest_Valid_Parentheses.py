# %% [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res, st = 0, [-1]
        for i, c in enumerate(s):
            if c == ")":
                st.pop()
                if st:
                    res = max(res, i - st[-1])
                    continue
            st.append(i)
        return res
