class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):return -1
        current = 0
        ans = 0
        for i in range(len(gas)):
            current +=gas[i]-cost[i]
            if current<0:
                current =0
                ans = i+1
        return ans