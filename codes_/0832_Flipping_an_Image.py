# %% [832. Flipping an Image](https://leetcode.com/problems/flipping-an-image/)
# 問題：水平方向にflipし、0-1を反転せよ
# 解法：numpy.flipを用いる
import numpy as np


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return (1 - np.flip(A, 1)).tolist()
