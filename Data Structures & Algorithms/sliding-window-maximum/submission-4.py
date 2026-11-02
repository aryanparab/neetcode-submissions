import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans =[]
        hp = []

        for i in range(k):
            heapq.heappush(hp,[-1*nums[i],i])
        ans.append(-1*hp[0][0])
        
        for i in range(1,len(nums)-k+1):
            while hp and hp[0][1]<i:
                heapq.heappop(hp)
            heapq.heappush(hp,[-1*nums[i+k-1],i+k-1])
            ans.append(-1*hp[0][0])
        return ans