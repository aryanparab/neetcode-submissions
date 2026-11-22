class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:return nums[0]

        def houserob(i,ss):
            if i>len(nums)-1:
                return ss
            k1 = houserob(i+1,ss)
            k2 = houserob(i+2,ss+nums[i])
            return max(k2,k1)
        return houserob(0,0)