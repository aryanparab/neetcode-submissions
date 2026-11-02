class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def tot(i,j):
            
            if i==len(word1) and j==len(word2):
                return 0
            # if i==len(word2):
            #     return 0
            if j==len(word2):
                return len(word1)-i
            if i ==len(word1):
                return len(word2)-j
            if (i,j) in memo:
                return memo[(i,j)]
            if word1[i]==word2[j]:
                memo[(i,j)] = tot(i+1,j+1)
                
            else:
                memo[(i,j)] = 1+ min( tot(i,j+1),tot(i+1,j),tot(i+1,j+1))
            return memo[(i,j)]
        return tot(0,0)
            