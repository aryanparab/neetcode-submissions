class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edge = {}
        
        for i,j in edges:
            if edge.get(i,-1)==-1:
                edge[i]=[]
            if edge.get(j,-1)==-1:
                edge[j]=[]
            edge[i].append(j)
            edge[j].append(i)
        isconnected = set()
        components=0
        def traverse(node):
            if node not in isconnected:
                isconnected.add(node)
                for i in edge[node]:
                    traverse(i)
            return 
        
        for i in edge.keys():
            if i not in isconnected:
                components+=1
                traverse(i)
       
        return components + n-len(isconnected)