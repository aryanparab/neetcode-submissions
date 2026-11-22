class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(curr):
            if state[curr]==1:
                return False
            if state[curr]==2:
                return True
            state[curr]=1
            for p in preq[curr]:
                if not dfs(p):
                    return False

            state[curr]=2
            order.append(curr)
            return True
            
        preq = {i:[] for i in range(numCourses)}

        for p in prerequisites:
            preq[p[0]].append(p[1])
        
        state = [0]*numCourses
        order = []
        for i in range(numCourses):
            if not dfs(i):
                return []


        return order
        