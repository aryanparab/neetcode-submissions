class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
       
        rotten = []
        fresh = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2 :
                    rotten.append([i,j])
                if grid[i][j]==1:
                    fresh.add((i,j))
        minute=0
        while rotten!=[]:
            minute+=1
            rotted =[]
            for i,j in rotten:
                for dx,dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                    if -1<i+dx<n and -1<j+dy<m and grid[i+dx][j+dy]==1:
                        fresh.remove((i+dx,j+dy))
                        grid[i+dx][j+dy]=2
                        rotted.append([i+dx,j+dy])
            
            rotten=rotted
        if fresh !=set():return -1
        return minute-1 if minute !=0 else 0

            
     
