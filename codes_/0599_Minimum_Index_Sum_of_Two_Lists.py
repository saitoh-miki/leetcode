# %% [599. Minimum Index Sum of Two Lists](https://leetcode.com/problems/minimum-index-sum-of-two-lists/)
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        order1 = {v: i for i, v in enumerate(list1, 1)}
        order = [(i + j, v) for j, v in enumerate(list2, 1) if (i := order1.get(v, 0))]
        mn = min(order)[0]
        return [i[1] for i in order if i[0] == mn]
