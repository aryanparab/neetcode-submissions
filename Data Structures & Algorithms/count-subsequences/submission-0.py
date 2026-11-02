class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ls,lt = len(s),len(t)
        m ={}
        def trav(i,j,c):
            if c==lt:
                return 1
            if i==ls or j==lt:
                return 0

            if (i,j,c) in m:
                return m[(i,j,c)]
            x1 = 0
            if s[i]==t[j]:
                x1 = trav(i+1,j+1,c+1)
            x2 = trav(i,j+1,c) + trav(i+1,j,c)+trav(i+1,j+1,c)
            m[(i,j,c)] = x1+x2
            return m[(i,j,c)]
        return trav(0,0,0)