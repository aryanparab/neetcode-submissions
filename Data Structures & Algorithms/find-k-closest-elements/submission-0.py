import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        hp = []
        ans = []
        for i in arr:
            ans.append([abs(i-x),i])
            heapq.heappush(hp,[abs(i-x),i])
            
        
        ans.sort(key=lambda x : [x[0],x[1]])
        m =  [ans[i][1] for i in range(k)]
        m.sort()
        return m
    