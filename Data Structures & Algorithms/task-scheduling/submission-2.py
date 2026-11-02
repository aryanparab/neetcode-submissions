import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task = {}
        for t in tasks:
            task[t] = task.get(t,0)+1
        heap = []
        for t in task.keys():
            heapq.heappush(heap,-1*task[t])
        cycle = 0
        q = deque()
        while heap or q:
            
            cycle+=1
            if not heap:
                cycle = q[0][1]
            else:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([cnt,cycle+n])
            if q and q[0][1]==cycle:
                heapq.heappush(heap,q.popleft()[0])

            
        return cycle