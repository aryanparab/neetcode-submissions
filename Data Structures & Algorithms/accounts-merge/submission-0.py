class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph ={}
        for acc in accounts:
            acc=acc[1:]
            for i in range(len(acc)):
                if acc[i] not in graph :
                        graph[acc[i]]=set()
                for j in range(1,len(acc)):
                    
                    if acc[j] not in graph:
                        graph[acc[j]] = set()
                    graph[acc[i]].add(acc[j])
                    graph[acc[j]].add(acc[i])
        def other_acc(i):
         
            if i in visited:
                return
            visited.add(i)
            for j in graph[i]:
                other_acc(j)
            return 
        ans = []
        for acc in accounts:
            name = acc[0]
            visited = set()
            for i in acc[1:]:
                other_acc(i)
            
            add = [name] + sorted([i for i in visited])
            if add not in ans:
                ans.append(add)
        return ans
