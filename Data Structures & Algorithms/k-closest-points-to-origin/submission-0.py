import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap =[]
        for i in points:
            heapq.heappush(heap,[(i[0]**2 + i[1]**2)**0.5,i])
        ans = []
        while k>0:
            ans.append(heapq.heappop(heap)[1])
            k-=1
        return ans