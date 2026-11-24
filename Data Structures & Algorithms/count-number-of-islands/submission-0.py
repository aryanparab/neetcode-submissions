class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def trav(i,j):
            if not -1<i<n or not -1<j<m or grid[i][j]!="1": return
            grid[i][j]="2"
            for dx,dy in [[0,1],[1,0],[0,-1],[-1,0]]:
                trav(i+dx,j+dy)
            return

        n,m = len(grid),len(grid[0])
        ans =0

        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    ans+=1
                    trav(i,j)
        return ans
        