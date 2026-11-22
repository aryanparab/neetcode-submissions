class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = len(nums)-1
        k = 0
        for i in range(len(nums)):
            if nums[i]==val:
                k+=1
                while nums[last]==val and i< last:
                    last-=1
                if i>last:break
                nums[i],nums[last]=nums[last],nums[i]
                
                last-=1
        return len(nums)-k
                