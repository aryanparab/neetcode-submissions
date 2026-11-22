import heapq
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:return 0
        heap = [-1*nums[0]]
        ans =0
        for i in range(1,len(nums)):
            print(heap)
            
            while heap:
                curr = -1* heapq.heappop(heap)
                if curr>=nums[i]:
                    continue
                heapq.heappush(heap,-1*curr)
                break
            heapq.heappush(heap,-1*nums[i])
            ans = max(ans,len(heap))

        return ans
        