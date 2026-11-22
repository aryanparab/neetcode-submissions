class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans =[]
        
        for i in range(len(nums)-k+1):
            curr_max =0
            for j in range(i,i+k):
                curr_max = max(curr_max,nums[j])
            ans.append(curr_max)
        return ans