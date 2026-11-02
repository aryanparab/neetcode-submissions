class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = [0 for _ in range(len(cost))]
        if len(cost)<3:
            return min(cost)
        ans[0],ans[1] = cost[0], cost[1]
        
        for i in range(2,len(cost)):
            ans[i] =cost[i]+ min(ans[i-1],ans[i-2])
        return min(ans[-1],ans[-2])