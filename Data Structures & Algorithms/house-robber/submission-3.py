class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums)<2:return nums[0]
        memo = {}
        def houserob(i,ss):
            if i>len(nums)-1:
                return ss
            if (i,ss) in memo:
                return memo[(i,ss)]
            k1 = houserob(i+1,ss)
            k2 = houserob(i+2,ss+nums[i])
            memo[(i,ss)] = max(k2,k1)
            return memo[(i,ss)]
        
        return houserob(0,0)