class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = set()
        for i in nums:
            if i in vals:
                return True
            vals.add(i)
        return False