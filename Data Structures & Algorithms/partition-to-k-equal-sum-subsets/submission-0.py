class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k > len(nums):return False
        if sum(nums)%k !=0:return False
        each= sum(nums)//k
        return True