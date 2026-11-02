import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht = {}
        for i in nums:
            ht[i] = ht.get(i,0)+1
        hp = []
        for key,v in ht.items():
            heapq.heappush(hp,[v,key])
       
            if len(hp)>k:
                heapq.heappop(hp)
        
        return [i[1] for i in hp]