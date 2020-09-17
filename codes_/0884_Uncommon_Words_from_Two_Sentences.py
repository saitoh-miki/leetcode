# %% [884. Uncommon Words from Two Sentences](https://leetcode.com/problems/uncommon-words-from-two-sentences/)
# 問題：AおよびBの中で1度しか出ない単語を返せ
# 解法：collections.Counterを用いる
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        c = collections.Counter(A.split() + B.split())
        return [s for s, n in c.items() if n == 1]
