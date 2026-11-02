class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edges = {i:set() for i in range(numCourses)}
        
        for i,j in prerequisites:
            
            edges[i].add(j)
        
        def reachable(current,goal):
            if current==goal:
                return True
            if current in st:return False
            st.add(current)
            for i in edges[current]:
                if reachable(i,goal):
                    return True
            return False
            
        res= []
        for i,j in queries:
            st = set()
            ans = reachable(i,j)
            res.append(ans)
        return res