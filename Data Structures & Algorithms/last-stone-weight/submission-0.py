import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = []
        for i in stones:
            heapq.heappush(hp,-1*i)
        while len(hp)>1:
            x,y = heapq.heappop(hp),heapq.heappop(hp)
            if x==y:continue
            heapq.heappush(hp,y-x)
        if len(hp)==1:
            return hp[0]
        return 0