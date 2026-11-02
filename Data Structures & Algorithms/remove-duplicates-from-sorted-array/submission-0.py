class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0,len(nums)-1
        visited = set()
        while l<len(nums):
            if nums[l] not in visited:
                visited.add(nums[l])
                l+=1
            else:
                r = l
                while r<len(nums) and nums[r] in visited:
                    r+=1
                if r==len(nums):break
                nums[l],nums[r]=nums[r],nums[l]
                
        return len(visited)