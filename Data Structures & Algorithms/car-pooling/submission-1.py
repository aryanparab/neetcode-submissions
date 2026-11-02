import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        curr_cap = 0
        hp = []
        for n,s,e in trips:
            while hp and hp[0][0]<=s:
                _,c = heapq.heappop(hp)
                curr_cap-=c
            if curr_cap + n > capacity:
                    return False
            heapq.heappush(hp,[e,n])
            curr_cap+=n
        return True
