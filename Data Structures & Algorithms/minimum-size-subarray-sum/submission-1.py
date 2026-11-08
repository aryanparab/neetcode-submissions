class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        ss =0
        ans = len(nums)+1
        while r<len(nums):
            ss+=nums[r]
            while ss>=target and l<=r:
                ans = min(ans,r-l+1)
                ss-=nums[l]
                l+=1
            r+=1
        return 0 if ans==len(nums)+1 else ans
