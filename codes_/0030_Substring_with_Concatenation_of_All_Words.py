# %% [30. Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        n, m = len(s), len(words[0])
        if n < (mm := m * len(words)):
            return []
        res = []
        cc = collections.Counter(words)
        n, m = len(s), len(words[0])
        cand = list(range(n - mm, -1, -1))
        while cand:
            i = cand.pop()
            for word in words:
                if s[i:].startswith(word):
                    c = cc.copy()
                    c[word] -= 1
                    k = i + m
                    while any(c.values()):
                        if not c[s[k : k + m]]:
                            break
                        c[s[k : k + m]] -= 1
                        k += m
                    else:
                        res.append(i)
                        break
            else:
                t = s[i : i + mm]
                cand = [k for k in cand if s[k : k + mm] != t]
        return res
