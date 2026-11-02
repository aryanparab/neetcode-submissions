class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def addorskip(i,ll):
            if i==len(nums):
                ans.append(list(ll))
                return
            ll.add(nums[i])
            addorskip(i+1,ll)
            ll.remove(nums[i])
            addorskip(i+1,ll)
            return 
        addorskip(0,set())
        return ans