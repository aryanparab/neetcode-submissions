class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx_s = nums[0]
        cs = 0
        for i in nums:
            if cs<0:
                cs =0
            cs+=i
            mx_s = max(mx_s,cs)
        return mx_s
