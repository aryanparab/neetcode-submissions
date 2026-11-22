class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def search_space(l,r,dt):
            if l>=r:return
      
            dt[nums[l]]-=1
            dt[nums[r]]-=1
            x = -1*(nums[l]+nums[r])
            
            if dt.get(x,0)!=0:
                ff = tuple(sorted([nums[l],nums[r],x]))
                ans.add(ff)
            search_space(l+1,r,dt)
            search_space(l,r-1,dt)
            return
        nums.sort()
        if nums[0]>0:return []
        if nums[-1]<0:return []
        dt = {}
        for i in nums:
            dt[i] = dt.get(i,0)+1
        l,r = 0, len(nums)-1
        search_space(l,r,dt)
        return [list(i) for i in ans]