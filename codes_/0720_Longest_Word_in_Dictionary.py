# %% [720. Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/)
# 問題：最も長く、辞書式順序で最初の単語を返せ。ただし、その単語を後ろから1文字ずつ短くした単語がすべてwordsに含まれていること
# 解法：ソート済みwordsを繰り返し、1文字短い単語が既出かチェックする
class Solution:
    def longestWord(self, words: List[str]) -> str:
        res, mx, st = "", 0, set()
        for word in sorted(words):
            n = len(word)
            if n == 1 or word[:-1] in st:
                st.add(word)
                if n > mx:
                    mx, res = n, word
        return res
