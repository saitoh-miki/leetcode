# %% [1282. Group the People Given the Group Size They Belong To](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/)
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans, dc = [], {}
        for i, v in enumerate(groupSizes):
            if v not in dc or len(dc[v]) == v:
                dc[v] = p = []
                ans.append(p)
            dc[v].append(i)
        return ans
