class Solution:
    total=0
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def summing(i,current):
            
            if i==len(nums):
                if current==target:
                    return 1
                return 0 
            if (i,current) in memo:return memo[(i,current)]
            memo[(i,current)] = summing(i+1,current+nums[i]) + summing(i+1,current-nums[i])
            return memo[(i,current)]
        
        return summing(0,0)