class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans  = min(nums)
        for i in range(len(nums)):
            current = 0
            for j in range(i,len(nums)):
                current+=nums[j]
                ans = max(ans,current)
        return ans
