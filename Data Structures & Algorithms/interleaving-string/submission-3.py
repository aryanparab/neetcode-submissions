class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def interleave(i,j,k):
            if k==len(s3):
                
                return (i == len(s1)) and (j == len(s2))
            if (i,j,k) in memo:
                return memo[(i,j,k)]
            
            if i<len(s1) and j<len(s2) and s1[i]==s3[k] and s2[j]==s3[k]:
                memo[(i,j,k)]= interleave(i+1,j,k+1) or interleave(i,j+1,k+1)
            elif i<len(s1) and s1[i]==s3[k]:
                memo[(i,j,k)]= interleave(i+1,j,k+1)
            elif j<len(s2) and s2[j]==s3[k]:
                memo[(i,j,k)]= interleave(i,j+1,k+1)
            return memo.get((i,j,k),False)
        return interleave(0,0,0)