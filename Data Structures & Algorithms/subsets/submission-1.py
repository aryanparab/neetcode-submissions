class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def addorskip(i,ll):
            if i==len(nums):
                ans.append(ll.copy())
                return
            ll.append(nums[i])
            addorskip(i+1,ll)
            ll.pop()
            addorskip(i+1,ll)
            return 
        addorskip(0,[])
        return ans