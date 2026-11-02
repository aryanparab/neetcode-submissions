class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = cur = 0
        ps = {0:1}
        
        for i in range(len(nums)):
            cur += nums[i]
            diff = cur-k
            res+= ps.get(diff,0)
            ps[cur] = 1+ps.get(cur,0)
        return res
        