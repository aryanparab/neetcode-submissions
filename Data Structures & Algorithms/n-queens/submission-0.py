from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def attackPositions(x,y):
            attacks = []
            dx,dy=x,y
            while dx+1<n :
                dx=dx+1
                attacks.append([dx,dy])
            dx=x
            while dy+1<n:
                dy=dy+1
                attacks.append([dx,dy])
            dy=y
            while dx-1>-1:
                dx-=1
                attacks.append([dx,dy])
            dx=x
            while dy-1>-1:
                dy-=1
                attacks.append([dx,dy])
            dy=y
            while dx+1<n and dy+1<n:
                dx+=1
                dy+=1
                attacks.append([dx,dy])
            dx,dy=x,y
            while dx+1<n and dy-1>-1:
                dx+=1
                dy-=1
                attacks.append([dx,dy])
            dx,dy=x,y
            while dx-1>-1 and dy+1<n:
                dx-=1
                dy+=1
                attacks.append([dx,dy])
            dx,dy=x,y
            while dx-1>-1 and dy-1>-1:
                dx-=1
                dy-=1
                attacks.append([dx,dy])
            
            attacks.append([x,y])
            return attacks

        def determine(queens, tx, ty, setup):
            if queens == 0:
                grid = [["." for _ in range(n)] for _ in range(n)]
                for i, j in setup:
                    grid[i][j] = "Q"
                ans.append(["".join(row) for row in grid])
                return

            if len(ap) < queens:
                return

            reach = attackPositions(tx, ty)
            newer_attacks = []
            for i, j in reach:
                if (i, j) in ap:
                    ap.remove((i, j))
                    newer_attacks.append([i, j])

            # ONLY pick candidates from lower rows to prevent permuting the same setup
            candidates = [pos for pos in list(ap) if pos[0] > tx]

            for i, j in candidates:
                setup.append([i, j])
                determine(queens - 1, i, j, setup)
                setup.pop()

            for i, j in newer_attacks:
                ap.add((i, j))

        ans = []
        
        # CHANGE 2: Fix starting positions to row 0 only to prevent duplicate solution permutations
        for j in range(n):
            ap = set((r, c) for r in range(n) for c in range(n))
            determine(n - 1, 0, j, [[0, j]])

        # Return the actual solutions list
        return ans