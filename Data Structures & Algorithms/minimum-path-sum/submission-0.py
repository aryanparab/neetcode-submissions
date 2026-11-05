class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        board = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        board[0][0]=grid[0][0]
        for i in range(1,len(grid[0])):
            board[0][i] = board[0][i-1]+grid[0][i]
        for i in range(1,len(grid)):
            board[i][0] = board[i-1][0]+grid[i][0]

        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                board[i][j] = grid[i][j]+min(board[i-1][j],board[i][j-1])
        return board[-1][-1]