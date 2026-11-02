class Solution:
    def countSubstrings(self, nums: str) -> int:
        res= 0
        for i in range(len(nums)):
            ans = 1
            n=1
            while i+n<len(nums) and i-n>-1 and nums[i+n]==nums[i-n]:
                ans+=1
                n+=1
            n=1
            if i+1!=len(nums) and nums[i]==nums[i+1]:
                ans+=1
                while (i+n+1)<len(nums) and i-n>-1 and nums[i+n+1]==nums[i-n]:
                    ans+=1
                    n+=1 
            res+=ans
        return res