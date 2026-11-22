class Solution:
    mx = 0
    def characterReplacement(self, s: str, k: int) -> int:
        prev,length =s[0],0
        
        def looper(i,prev,k,l):
            if i==len(s):
                self.mx = max(l,self.mx)
                return
            if prev==s[i]:
                return looper(i+1,prev,k,l+1)
           
            if k>0:
                looper(i+1,prev,k-1,l+1)
            else:
                self.mx = max(l,self.mx)

            looper(i+1,s[i],k,0)
            return
        looper(0,prev,k,0)
        return self.mx