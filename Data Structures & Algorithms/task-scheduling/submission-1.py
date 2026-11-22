import heapq
import math
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task = {}
        for t in tasks:
            task[t] = task.get(t,0)+1
        heap = []
        for t in task.keys():
            heapq.heappush(heap,[task[t],t,0])
        cycle = 1
        while heap:
            temp = []
            mn = float('inf')
            while heap and heap[0][2]>cycle:
                x = heapq.heappop(heap)
                mn = min(mn,x[2])
                temp.append(x)
            if not heap:
                ad = math.ceil(mn/n)
                cycle += ad+1
            else:
                x = heapq.heappop(heap)
                cycle+=1
                if x[0]-1!=0:
                    temp.append([x[0]-1,x[1],x[2]+n])
            for i in temp:
                heapq.heappush(heap,i)
            
        return cycle