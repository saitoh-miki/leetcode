# %% [867. Transpose Matrix](https://leetcode.com/problems/transpose-matrix/)
# 問題：Aを転置せよ
# 解法：numpy.transposeを用いる
import numpy as np


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return np.transpose(A).tolist()
