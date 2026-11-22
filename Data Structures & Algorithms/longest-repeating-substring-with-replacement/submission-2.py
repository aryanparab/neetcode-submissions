class Solution:
    
    def characterReplacement(self, s: str, k: int) -> int:
        xs = {}
        mx = ["",0]
        for i in range(len(s)):
            xs[s[i]] = xs.get(s[i],0)+1
            if mx[1]<xs[s[i]]:
                mx=[s[i],xs[s[i]]]
        
        lc = []
        ans = 0
        start = 0
        for i in range(len(s)):
            if s[i]==mx[0]:
                continue
            elif k>0:
                k-=1
                lc.append(i)
            else:
                ans = max(ans, i-start)
                if lc==[]:
                    return i
                i=lc.pop(0)+1
                start = i
                k=1
        if start ==0:return len(s)
        return ans        
