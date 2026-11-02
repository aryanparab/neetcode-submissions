class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def connect(i,j):
            if i==-1 or i==m or j==-1 or j==n:
                return 
            if (i,j) in connected:return 
            if board[i][j]=="O":
                connected.add((i,j))
                connect(i+1,j)
                connect(i,j+1)
                connect(i-1,j)
                connect(i,j-1)
            return
        connected = set()
        m,n = len(board),len(board[0])
        for i in range(n):
            if board[0][i]=="O":
                connect(0,i)
            
            if board[m-1][i]=="O":
                connect(m-1,i)
        for i in range(m):
            if board[i][0]=="O":
                connect(i,0)
            if board[i][n-1]=="O":
                connect(i,n-1)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O" and (i,j) not in connected:
                    board[i][j]="X"
        