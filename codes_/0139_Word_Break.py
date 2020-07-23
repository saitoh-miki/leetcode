# %% [139. Word Break](https://leetcode.com/problems/word-break/)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @functools.lru_cache(None)
        def check(s):
            if not s:
                return True
            for word in wordDict:
                if s.startswith(word) and check(s[len(word):]):
                    return True
            return False
        return check(s)
