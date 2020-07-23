# %% [167. Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if (s := numbers[i] + numbers[j]) == target:
                return [i + 1, j + 1]
            elif s > target:
                j -= 1
            else:
                i += 1
