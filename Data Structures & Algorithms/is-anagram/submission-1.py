class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        x,y= {},{}
        for i in range(len(s)):
            x[s[i]]=x.get(s[i],0)+1
            y[t[i]]=y.get(t[i],0)+1
        for i in x:
            
            if x[i]!=y.get(i,-1):return False
        return True
