class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #connected and has no cycles 
        def travel(node,prev):
            if node in visited:
                return False
            visited.add(node)
            for i in edg[node]:
                if i == prev:continue
                if not travel(i,node):
                    return False
            return True

        edg = {i:[] for i in range(n)}
        for i,j in edges:
            edg[i].append(j)
            edg[j].append(i)
        visited = set()
        x = travel(0,-1)
        return x and len(visited)==n

