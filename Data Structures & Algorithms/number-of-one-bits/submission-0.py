class Solution:
    def hammingWeight(self, n: int) -> int:
        s=0
        while n:
            s+=n%2
            n=n//2
        
        return s