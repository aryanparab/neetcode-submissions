class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        def find_arrs(i,curr_s):
            if curr_s==k:
                ans.append(1)
            if i==len(nums):
                return
            
            find_arrs(i+1,curr_s+nums[i])
            return
            
        
        ans = []
        for i in range(len(nums)):
            find_arrs(i+1,nums[i])
        return sum(ans)