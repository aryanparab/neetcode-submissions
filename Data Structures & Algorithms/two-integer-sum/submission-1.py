class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ss = {}
        for i in range(len(nums)):
            if ss.get(target-nums[i],-1)!=-1  and i!=ss[target-nums[i]]:
                return [ss[target-nums[i]],i]
            ss[nums[i]]=i
            
            
        print(ss)
