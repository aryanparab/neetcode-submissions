class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
            def find(i,dr,x,y,word):
                
                if i==len(word):
                    return True

                for dx,dy in [[0,1],[1,0],[0,-1],[-1,0]]:
                    if [dx,dy]==dr:continue
                    if -1<x+dx<len(board) and -1<y+dy<len(board[0]) and board[x+dx][y+dy]==word[i]:
                        c = find(i+1,[dx*-1,dy*-1],x+dx,y+dy,word)
                        if c:
                            return True
                return False
            ans = []
            for m in words:
                word = m
                for i in range(len(board)):
                    for j in range(len(board[0])):
                        c= find(0,[-1,-1],i,j,word)
                        if c:
                            ans.append(word)
                            break
                    if word in ans:
                        break

            return ans
