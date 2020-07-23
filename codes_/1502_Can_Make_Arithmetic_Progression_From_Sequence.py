# %% [1502. Can Make Arithmetic Progression From Sequence](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/)
[](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/)
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        lst = [j - i for i, j in zip(arr, arr[1:])]
        return all(i == lst[0] for i in lst[1:])
