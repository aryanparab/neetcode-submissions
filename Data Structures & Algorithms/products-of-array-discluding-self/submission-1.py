class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = [1 for i in range(len(nums))]
        p[0]=1
        for i in range(1,len(nums)):
            p[i]=p[i-1]*nums[i-1]
        s= [1 for i in range(len(nums))]
        s[-1]=1
        for i in range(len(nums)-2,-1,-1):
            s[i]=s[i+1]*nums[i+1]
        r = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            r[i]=p[i]*s[i]
        return r