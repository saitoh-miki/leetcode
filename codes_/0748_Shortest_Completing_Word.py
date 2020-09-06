# %% [748. Shortest Completing Word](https://leetcode.com/problems/shortest-completing-word/)
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        co = collections.Counter(c.lower() for c in licensePlate if c.isalpha())
        dc = collections.defaultdict(list)
        for word in words:
            dc[len(word)].append(word)
        for n in sorted(dc):
            for word in dc[n]:
                if not (co - collections.Counter(word)):
                    return word
