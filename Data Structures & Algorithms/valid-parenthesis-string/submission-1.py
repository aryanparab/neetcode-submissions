class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def ct(i,cts):
            if cts<0:return False
            if i==len(s):
                return True if cts==0 else False
            if (i,cts) in memo:
                return memo[(i,cts)]
            if s[i]=="(":
                memo[(i,cts)] =  ct(i+1,cts+1)
            elif s[i]==")":
                memo[(i,cts)]=  ct(i+1,cts-1)
            else:
                memo[(i,cts)] =  ct(i+1,cts-1) or ct(i+1,cts+1) or ct(i+1,cts)
            return memo[(i,cts)]
        return ct(0,0)