class Solution:
    def reverseBits(self, n: int) -> int:
        
        n = bin(n)[2:]
        while len(n)!=32:
            n= "0"+n
        ans =0
  
        for i in range(len(n)):
            
            ans += (2**i)*int(n[i])
        return ans