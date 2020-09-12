# %% [766. *Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/)
# 問題：すべての対角成分がすべて同じかどうかを返せ
# 解法：右下の要素と異ならないかを調べる
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n, m = len(matrix), len(matrix[0])
        for i in range(n - 1):
            for j in range(m - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
