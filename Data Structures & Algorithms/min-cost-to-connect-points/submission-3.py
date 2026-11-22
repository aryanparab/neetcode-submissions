import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int: 
        if len(points)==1:
            return abs(points[0]-points[1])
        hp =[]
        for i,j in points:
            heapq.heappush(hp,[abs(i+j),[i,j]])
        ans = 0 
        while len(hp)>1:
            
            x1,p1 = heapq.heappop(hp)
            x2,p2 = heapq.heappop(hp)
            ans += abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
            heapq.heappush(hp,[x2,p2])
        return ans