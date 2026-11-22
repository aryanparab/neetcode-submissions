class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cg = {}
        for i,j in prerequisites:
            if cg.get(i,0)==0:
                cg[i]=[]
            cg[i].append(j)
        def has_cycle(i):
            if i in path:return False
            path.add(i)
            if cg.get(i,0)==0:
                return True
            for n in cg[i]:
                return has_cycle(n)

        for i in range(numCourses):
            if cg.get(i,0)!=0:
                path = set()

                if  not has_cycle(i):
                    return False
        return True
