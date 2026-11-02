class Solution:
    ans = [0,""]
    def longestPalindrome(self, s: str) -> str:
       
        def check_pal(i,j):
            if i<0 or j==len(s) or s[i]!=s[j] :
                if self.ans[0]<j-i-1:
                    self.ans = [j-i-1,s[i+1:j]]
               
                return
           
            if s[i]==s[j]:
                return check_pal(i-1,j+1)
        if len(s)==1:return s
        self.ans =[1,s[0]]
        ls = len(s)
        for i in range(len(s)):
            check_pal(i-1,i+1)
            if i<ls-1 and s[i]==s[i+1]:
                
                check_pal(i-1,i+2)
        return self.ans[1]
            
    