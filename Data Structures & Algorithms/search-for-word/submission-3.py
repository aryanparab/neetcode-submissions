class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        n,m = len(board),len(board[0])
        def travel(x,i,j):
            if x==len(word):
                
                return True
            if not -1<i<n or not -1<j<m:return False
            if (i,j) in visited:return False
            visited.add((i,j))
            if word[x]==board[i][j]:
                for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
                    if travel(x+1,i+di,j+dj):
                        return True
            visited.remove((i,j))
            return False
        for i in range(n):
            for j in range(m):
                if word[0]==board[i][j]:
                    visited = set()
                    visited.add((i,j))
                    for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
                        if travel(1,i+di,j+dj):
                            return True
        return False

                