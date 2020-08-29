# %% [167. *Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
# 問題：リスト中の2つの要素の和がtargetになるインデックスを列挙せよ
# 解法：両端から片方ずつ変えながら探索する
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
