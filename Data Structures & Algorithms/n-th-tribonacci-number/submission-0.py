class Solution:
    def tribonacci(self, n: int) -> int:
        if n<3:
            return 1 if n!=0 else 0
        p1,p2,p3 =0,1,1
        curr = 0
        for i in range(n-2):
            curr = p1+p2+p3
            p1,p2,p3 = p2,p3,curr
        return curr