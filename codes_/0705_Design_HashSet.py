# %% [705. Design HashSet](https://leetcode.com/problems/design-hashset/)
class MyHashSet(set):
    remove = set.discard
    contains = set.__contains__
