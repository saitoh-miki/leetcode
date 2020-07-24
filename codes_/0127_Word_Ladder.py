# %% [127. Word Ladder](https://leetcode.com/problems/word-ladder/)
class Solution:
    def ladderLength(self, begin: str, end: str, words: List[str]) -> int:
        n, q, s = 1, [begin], set(words)
        while q and end not in q:
            n, q, r = n + 1, [], q
            while r:
                p = r.pop()
                for w in list(s):
                    if neig(p, w):
                        if w == end:
                            return n
                        q.append(w)
                        s.remove(w)
        return 0


def neig(w1, w2):
    n = 0
    for c1, c2 in zip(w1, w2):
        n += c1 != c2
        if n > 1:
            return False
    return True
