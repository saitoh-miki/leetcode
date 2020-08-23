# %% [500. *Keyboard Row](https://leetcode.com/problems/keyboard-row/)
class Solution:
    def *findWords(self, words: List[str]) -> List[str]:
        p = "([qwertyuiop]+|[asdfghjkl]+|[zxcvbnm]+)$"
        return [w for w in words if re.match(p, w, re.I)]
