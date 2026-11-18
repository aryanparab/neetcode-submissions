class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        ed = {i:[] for i in range(n)}
        def get_h(node,current_h,prev):
            h = current_h
            for i in ed[node]:
                if i==prev:continue
                h = max(h,get_h(i,current_h+1,node))
            return h
            
        for i,j in edges:
            ed[i].append(j)
            ed[j].append(i)
        ans = [float('inf'),[]]
        for i in range(n):
            height = get_h(i,0,-1)
            if height<ans[0]:
                ans = [height,[i]]
            elif height==ans[0]:
                ans[1].append(i)
        return ans[1]
            
            