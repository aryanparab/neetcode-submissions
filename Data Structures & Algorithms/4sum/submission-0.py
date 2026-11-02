class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans =set()
        l,r = 0 , len(nums)-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for l in range(k+1,len(nums)):
                        t = nums[i] + nums[j]+nums[k]+nums[l]
                        if t ==target:
                            ans.add((nums[i],nums[j],nums[k],nums[l]))
                        if t>target:
                            break
        return [list(o) for o in ans]