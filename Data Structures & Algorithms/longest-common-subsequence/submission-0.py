class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def check(i,j,cs):
            if len(text1)==i or len(text2)==j:
                return cs
            if (i,j,cs) in memo:
                return memo[(i,j,cs)]
            if text1[i]==text2[j]:
                memo[(i,j,cs)] = max(check(i+1,j,cs+1), check(i,j+1,cs+1))
            else:
                memo[(i,j,cs)] = max(check(i+1,j,cs), check(i,j+1,cs))
            return memo[(i,j,cs)]
        
        return check(0,0,0)
                