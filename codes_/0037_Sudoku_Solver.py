# %% [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)
import numpy as np


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        bd = np.vectorize(ord)(board) - 48
        solve(bd)
        board[:] = np.vectorize(chr)(bd + 48).tolist()


def solve(bd):
    i, j = bd.argmin() // 9, bd.argmin() % 9
    if bd[i, j] > 0:
        return True
    for n in range(1, 10):
        p, q = i - i % 3, j - j % 3
        if (
            (bd[i] == n).any()
            or (bd[:, j] == n).any()
            or (bd[p : p + 3, q : q + 3] == n).any()
        ):
            continue
        bd[i][j] = n
        if solve(bd):
            return True
        bd[i][j] = -2
    return False
