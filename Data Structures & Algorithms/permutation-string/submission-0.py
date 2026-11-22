class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1d = {}
        s2d = {}
        l = len(s1)
        for i in s1:
            s1d[i] = s1d.get(i,0)+1
            s2d[i] = 0
        if l>len(s2):return False
       
        for j in range(l):
            if s2d.get(j,-1)!=-1:
                s2d[j]+=1
        for i in range(l,len(s2)):
            print(s2d,s1d)
            if s2d==s1d:return True
            c,n = s2[i],s2[l-i-1]
            if s2d.get(c,0)!=0:
                s2d[c]-=1
            if s2d.get(n,-1)!=-1:
                s2d[n]+=1
        return False

