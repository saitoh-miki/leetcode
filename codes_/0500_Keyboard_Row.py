# %% [500. *Keyboard Row](https://leetcode.com/problems/keyboard-row/)
# 問題：キーボードの1列で入力可能な単語を求めよ
# 解法：正規表現を用いる
class Solution:
    def *findWords(self, words: List[str]) -> List[str]:
        p = "([qwertyuiop]+|[asdfghjkl]+|[zxcvbnm]+)$"
        return [w for w in words if re.match(p, w, re.I)]
