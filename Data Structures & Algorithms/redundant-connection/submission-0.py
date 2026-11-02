class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        e = {}
        for i,j in edges:
            if i not in e:
                e[i]=[]
            e[i].append(j)
            if j not in e:
                e[j]=[]
            e[j].append(i)
        def trav(i,prev):
            if i in visited:
                potential.append([i,prev])
                return
            visited.add(i)
            for n in e[i]:
                if n!=prev:
                    trav(n,i)
            return
        
        potential = []
        for i,_ in edges:
            visited =set()
            trav(i,-1)
        for i in edges[::-1]:
            if i in potential:
                return i
        

