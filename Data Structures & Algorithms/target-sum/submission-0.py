class Solution:
    total=0
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def summing(i,current):
            if i==len(nums):
                if current==target:
                    self.total+=1
                return
            summing(i+1,current+1)
            summing(i+1,current-1)
            return 
        summing(0,0)
        return self.total