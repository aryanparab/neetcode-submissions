class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grida = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        found = False
        for i in range(len(obstacleGrid)):
            if not found:
                if obstacleGrid[i][0]!=1:
                    grida[i][0] = 1
                    
                else:
                    found = True
                    grida[i][0] = -1
            else:
                grida[i][0] = -1
        found = False
        for i in range(len(obstacleGrid[0])):
            if not found:
                if obstacleGrid[0][i]!=1:
                    grida[0][i] = 1
                    
                else:
                    grida[0][i] = -1
                    found = True
            else:
                grida[0][i] = -1

        for i in range(1,len(grida)):
            for j in range(1,len(grida[0])):
                if obstacleGrid[i][j]==1:
                    grida[i][j]=-1
                else:
                    if grida[i-1][j]==-1 or grida[i][j-1]==-1:
                        grida[i][j]=max(grida[i-1][j],grida[i][j-1])
                    else:
                        grida[i][j] = grida[i][j-1]+grida[i-1][j]
        return 0 if grida[-1][-1]==-1 else grida[-1][-1]