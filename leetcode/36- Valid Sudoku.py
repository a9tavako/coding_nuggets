import math
from typing import List


n = 9
cell_size = round(math.sqrt(n))

def coord_to_cell(row: int, col:int) -> int:
    return cell_size * (row // cell_size) + (col // cell_size)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return False
        
        rows = [[0 for _ in range(n+1)] for _ in range(n+1)]
        cols = [[0 for _ in range(n+1)] for _ in range(n+1)]
        cells = [[0 for _ in range(n+1)] for _ in range(n+1)]

        for row in range(n):
            for col in range(n):
                if board[row][col] == ".":
                    continue

                val = int(board[row][col])
                if not (1 <= val <= n):
                    return False

                cell = coord_to_cell(row, col)
                if rows[row][val] != 0 or cols[col][val] != 0 or cells[cell][val] != 0:
                    return False

                rows[row][val] = 1
                cols[col][val] = 1
                cells[cell][val] = 1

        return True