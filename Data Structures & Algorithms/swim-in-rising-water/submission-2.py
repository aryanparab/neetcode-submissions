import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        hp =[]
        n,m= len(grid),len(grid[0])
        heapq.heappush(hp,(grid[0][0],0,0))
        visited = set()
        while hp:
            e,x,y = heapq.heappop(hp)
            if x==n-1 and y==m-1:return e
            for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                i,j = x+di,y+dj
                if -1==i or n==i or m==j or -1==j:continue
                if (i,j) in visited:continue
                visited.add((i,j))
                heapq.heappush(hp,(max(grid[i][j],e),i,j))
        return 

