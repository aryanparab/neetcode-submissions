class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target =len(nums)//3
        d = {}
        ans = []
        for i in nums:
            d[i] = d.get(i,0)+1
        for i in d.keys():
            if d[i]>target:
                ans.append(i)
        return ans