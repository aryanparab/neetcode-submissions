import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        kk = {}
       
        
        for i,j,f in times:
            if i not in kk:
                kk[i] = []
            kk[i].append([j,f])
        min_heap = [(0,k)]
        shortest = {}
        while min_heap:
            w1,n1 = heapq.heappop(min_heap)
            if n1  in shortest:continue
            shortest[n1]= w1
            for n2,w2 in kk.get(n1,[]):
                if n2 not in shortest:
                    heapq.heappush(min_heap,[w2+w1,n2])
        if len(shortest)==n:
            return max(shortest.values())        
        return -1 