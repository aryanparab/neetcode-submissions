class Solution:
    def climbStairs(self, n: int) -> int:
        nn = [0 for i in range(n+1)]
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        nn[1],nn[2] = 1,2
        for i in range(3,n+1):
            nn[i] = nn[i-1]+nn[i-2]
        return nn[-1]