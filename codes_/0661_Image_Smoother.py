# %% [661. *Image Smoother](https://leetcode.com/problems/image-smoother/)
# 問題：画像のピクセルを広げた3x3の範囲の平均（切り下げ）求めよ
# 解法：外側にNaNで広げnumpy.nanmeanを用いる
import numpy as np


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        n, m, r3 = len(M), len(M[0]), range(3)
        a = np.full((n + 2, m + 2), np.nan)
        a[1:-1, 1:-1] = M
        b = np.array([a[i : n + i, j : m + j] for i in r3 for j in r3])
        return np.nanmean(b, 0).astype(int).tolist()
