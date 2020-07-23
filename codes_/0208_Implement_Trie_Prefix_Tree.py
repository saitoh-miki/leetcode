# %% [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

def factory():
    return collections.defaultdict(factory)

class Trie:
    def __init__(self):
        self.data = factory()
    def insert(self, word: str) -> None:
        t = self.data
        for c in word:
            t = t[c]
        t['$'] = None
    def search(self, word: str, ing=False) -> bool:
        t = self.data
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return ing or '$' in t
    def startsWith(self, word: str) -> bool:
        return self.search(word, True)
