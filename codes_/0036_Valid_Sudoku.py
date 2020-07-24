# %% [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)
import numpy as np


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board = np.array(board)
        for i in range(9):
            j, k = (i // 3) * 3, (i % 3) * 3
            if ng(board[i]) or ng(board[:, i]) or ng(board[j : j + 3, k : k + 3]):
                return False
        return True


def ng(a):
    a = [c for c in a.flat if c != "."]
    return len(a) > len(set(a))
