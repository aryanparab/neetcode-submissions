class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotten = []
        freshes =set()
        n,m= len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    rotten.append([i,j])
                if grid[i][j]==1:
                    freshes.add((i,j))
        minute =0 
        
        while freshes:
            minute+=1
            new_rot = []
            while rotten:
                i,j = rotten.pop(0)
                for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                    x,y = i+dx,j+dy
                    if x ==n or x==-1 or y==m or y==-1:continue
                    if grid[x][y]==1:
                        
                        freshes.remove((x,y))
                        new_rot.append([x,y])
                        grid[x][y]=2
            rotten = new_rot
            if rotten==[]:break

        if len(freshes)>0:return -1
        return minute

            
