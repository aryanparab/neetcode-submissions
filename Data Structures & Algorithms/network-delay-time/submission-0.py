class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        kk = {}
        time = {i:float('inf') for i in range(1,n+1)}
        
        def trav(node,prev_time):
            
            if prev_time>time[node]:
                return 
            time[node] = prev_time
            
            for i,j in kk.get(node,[]):
                trav(i,prev_time + j)
            
            return 

        for i,j,f in times:
            if i not in kk:
                kk[i] = []
            kk[i].append([j,f])

        trav(k,0)
        ans = 0

        for i in time.values():
            ans = max(ans,i)
        return -1 if ans==float('inf') else ans