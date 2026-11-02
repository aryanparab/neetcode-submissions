class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def explore(x,y):
            if x==-1 or x==n or y==-1 or y==m:
                return 0
            if grid[x][y]==0 or (x,y) in visited:
                return 0
            visited.add((x,y))
            aa =0
            for dx,dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                aa+=explore(x+dx,y+dy)
            return aa+1

        area =0
        n,m = len(grid),len(grid[0])
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and (i,j) not in visited:
                    area = max(area,explore(i,j))
        return area
