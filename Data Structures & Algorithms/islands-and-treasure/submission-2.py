class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def trav(x,y,dist):
            
            if x==m or x==-1 or y==n or y==-1:
                return 
            if dist>grid[x][y]:return
            
            if grid[x][y]!=-1:
                grid[x][y]=min(grid[x][y],dist)
            
                for dx,dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                    trav(x+dx,y+dy,dist+1)
            return 

        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                   
                    trav(i,j,0)