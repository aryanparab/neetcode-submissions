class Solution:
    def jump(self, nums: List[int]) -> int:
        #  0 2 4 1 1 1 1 
        #0 0 0 0 0 0 0 0 
        #2 0 0 1 1 0 0 0
        #4   0 1 1 2 2 2
        #1   0 0 1 2 2 2
        #1   0 0 0  
        #1
        #1

        n= len(nums)+1
        grid = [[0 for _ in range(n)] for _ in range(n)]
        grid[1][1] = 0
        nums = [0]+nums
        
        for i in range(1,n):
            grid[i][i] = grid[i-1][i]
            max_index = nums[i]+i
            for j in range(i+1,n):
                if j>max_index:
                    for k in range(j,n):
                        grid[i][k]=grid[i-1][k]
                    break
                if grid[i-1][j]==0:
                    grid[i][j] = 1+grid[i][i]
                else:
                    grid[i][j] = min(1+grid[i][i], grid[i-1][j])
        return grid[-1][-1]


