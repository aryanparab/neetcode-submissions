class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ss = {}
        for i in range(len(nums)):
            ss[nums[i]]=i
            
            if ss.get(target-nums[i],-1)!=-1  and i!=ss[target-nums[i]]:
                return [ss[target-nums[i]],i]
        print(ss)
