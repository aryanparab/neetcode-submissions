class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k > len(nums):return False
        if sum(nums)%k !=0:return False
        each= sum(nums)//k
        ll = [each for _ in range(k)]
        def dfs(i,ll):
            if i==len(nums):
                if sum(ll)==0:return True
                return False
            for j in range(len(ll)):
                ll[j] = ll[j]-nums[i]
                if dfs(i+1,ll):return True
                ll[j]= ll[j]+nums[i]
            return False
        return dfs(0,ll)