class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        x=[0 for i in range(len(cost))]
        if len(cost)<3:
            return min(cost)
        x[0],x[1]=cost[0],cost[1]
        for i in range(2,len(cost)):
            x[i]= cost[i]+min(x[i-1],x[i-2])
        return min(x[-1],x[-2])