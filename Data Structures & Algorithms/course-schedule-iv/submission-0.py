class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edges = {i:[] for i in range(numCourses)}
        prer = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            
            edges[i].append(j)
            for k in edges[j]:
                edges[i].append(k)
        res= []
        for i,j in queries:
            if j in edges[i]:
                res.append(True)
            else:
                res.append(False)
        return res