class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        effort = {}
        dfs = [[0,0,0]]
        n,m = len(heights),len(heights[0])
        while dfs:
            i,j,diff = dfs.pop(0)
            if (i,j) in effort and effort[(i,j)]<=diff:continue
            effort[(i,j)]=diff
            for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
                if -1==i+di or i+di==n or j+dj==-1 or j+dj==m:continue
                dfs.append([i+di,j+dj,max(diff,abs(heights[i][j]-heights[i+di][j+dj]))])
    
        return effort[(n-1,m-1)]
