class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = -float('inf')
        for i in range(len(nums)):
            tt = nums[i]
            mx = max(mx,tt)
            for j in range(i+1,len(nums)):
                tt*=nums[j]
                mx = max(mx,tt)
        return mx