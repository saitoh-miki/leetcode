# %% [804. Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words/)
# 問題：wordsの各単語からモールス信号を作成し、その種類数を返せ
# 解法：ordを用いる
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mc = (
            ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- "
            "-. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
        ).split()
        return len(set("".join(mc[ord(c) - 97] for c in word) for word in words))
