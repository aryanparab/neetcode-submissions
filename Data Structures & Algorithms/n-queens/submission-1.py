from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        
        # Track occupied columns and diagonals in O(1) time
        cols = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                ans.append(["".join(row) for row in board])
                return

            for c in range(n):
                # O(1) attack check
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # Place queen
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # Advance to the next row
                backtrack(r + 1)

                # Remove queen (Backtrack)
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return ans