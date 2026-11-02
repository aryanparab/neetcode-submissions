class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xx = {}
        for i in nums:
            xx[i] = xx.get(i,0)+1
        return [i for i in xx.keys() if xx[i]==1][0]