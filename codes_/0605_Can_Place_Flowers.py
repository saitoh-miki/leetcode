# %% [605. Can Place Flowers](https://leetcode.com/problems/can-place-flowers/)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        lst = [(w, len(list(a))) for w, a in itertools.groupby(flowerbed)]
        if len(lst) == 1:
            return n * lst[0][0] == 0 and (lst[0][1] + 1) // 2 >= n
        if lst and lst[0][0] == 0:
            lst = [(1, 0), (0, lst[0][1] + 1)] + lst[1:]
        if lst and lst[-1][0] == 0:
            lst = lst[:-1] + [(0, lst[-1][1] + 1), (1, 0)]
        ttl = sum((i[1] - 1) // 2 for i in lst[1::2])
        return ttl >= n
