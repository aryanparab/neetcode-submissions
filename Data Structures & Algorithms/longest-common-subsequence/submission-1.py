class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def check(i,j):
            if len(text1)==i or len(text2)==j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if text1[i]==text2[j]:
                memo[(i,j)] = 1+  max(check(i+1,j+1), check(i+1,j+1))
            else:
                memo[(i,j)] = max(check(i+1,j), check(i,j+1))
            return memo[(i,j)]
        
        return check(0,0)
                