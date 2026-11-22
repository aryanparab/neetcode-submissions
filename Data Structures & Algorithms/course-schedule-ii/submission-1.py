class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def detect_cycle(curr):
            if curr in visited:return True
            visited.add(curr)
            for i in preq[curr]:
                if detect_cycle(i):return True
            visited.remove(curr)
            return False
            
        preq = {i:[] for i in range(numCourses)}

        for p in prerequisites:
            preq[p[0]].append(p[1])
        print(preq)
        for i in range(numCourses):
            visited = set()
            if detect_cycle(i):return []
        
        order= []
        added = set()
        for i in preq.keys():
            for j in preq[i]:
                order.append(j)
                added.add(j)
        for i in range(numCourses):
            if i not in added:
                order.append(i)
                added.add(i)
        print(order)
        return order
        