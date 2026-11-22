class Solution:
    ans = [0,""]
    def longestPalindrome(self, s: str) -> str:
        memo = {}
        def check_pal(i,j):
            if i<0 or j==len(s) or s[i]!=s[j] :
                if self.ans[0]<j-i-2:
                    self.ans = [j-i-2,s[i+1:j]]
                memo[(i,j)] = self.ans
                return
            if (i,j) in memo:return memo[(i,j)]
            if s[i]==s[j]:
                return check_pal(i-1,j+1)
        if len(s)==1:return s
        ls = len(s)
        for i in range(len(s)):
            check_pal(i-1,i+1)
            if i<ls-1 and s[i]==s[i+1]:
                check_pal(i-1,i+2)
        return self.ans[1]
            
    