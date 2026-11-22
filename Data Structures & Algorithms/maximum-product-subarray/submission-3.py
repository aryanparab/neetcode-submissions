class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = nums[0]
        track = nums[0]
        for i in range(1,len(nums)):
            # print(mx)
            mx = max(mx,nums[i]*track,nums[i])
            if nums[i]==0:
                track = nums[i]
            else:
                track = max(nums[i]*track,nums[i])
        nums = nums[::-1]
        track = nums[0]
        for i in range(1,len(nums)):
            # print(mx)
            mx = max(mx,nums[i]*track,nums[i])
            if nums[i]==0:
                track = nums[i]
            else:
                track = max(nums[i]*track,nums[i])
        return mx