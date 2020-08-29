# %% [32. **Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)
# 問題：括弧が有効な最大長を求める
# 解法：スタックに有効な開始位置候補を入れておく。括弧閉じ時に更新
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
