class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cg = {}
        for i,j in prerequisites:
            if cg.get(i,0)==0:
                cg[i]=[]
            cg[i].append(j)

        state = [0] * numCourses

        def has_cycle(i):
            if state[i] == 1:
                return True  # Cycle detected
            if state[i] == 2:
                return False  # Already verified safe

            state[i] = 1  # Mark as currently visiting

            for neighbor in cg.get(i,[]):
                if has_cycle(neighbor):
                    return True

            state[i] = 2  # Mark as fully visited
            return False

        for i in range(numCourses):
            if cg.get(i,0)!=0:
                path = set()
                if   has_cycle(i):
                    return False
        return True
