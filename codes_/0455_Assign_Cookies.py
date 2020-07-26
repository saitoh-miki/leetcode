# %% [455. Assign Cookies](https://leetcode.com/problems/assign-cookies/)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort(reverse=True)
        for i, v in enumerate(sorted(g)):
            c = 0
            while s and c < v:
                c = s.pop()
            if v > c:
                return i
        return i + 1
