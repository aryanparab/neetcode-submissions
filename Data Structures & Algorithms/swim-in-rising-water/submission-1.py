class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        timings = {}
        n,m = len(grid),len(grid[0])
        def swimmer(i,j,t):
            
            
            if i==n-1 and j==m-1:
                timings[(i,j)] = min(t,timings.get((i,j),float('inf')))
                return
            
            if (i,j) in timings and timings[(i,j)]<=t:return

            timings[(i,j)] =t
            for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
                x,y = i+di,j+dj
                if x==-1 or x==n or y==-1 or y==m:continue
                if t<grid[x][y]:
                    swimmer(x,y,t+(grid[x][y]-t))
                else:
                    swimmer(x,y,t)
            return
        swimmer(0,0,grid[0][0])
        
        return timings[(n-1,m-1)]