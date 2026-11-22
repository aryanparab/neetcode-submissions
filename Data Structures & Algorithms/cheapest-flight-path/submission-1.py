class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        fl = {}
        def fly(current,curr_p,stops):
            # print(visited,current,curr_p)
            if current == dst and stops<=k+1:
                
                visited[dst] = min(visited[dst],curr_p)
                return
            if stops>k:return
            if current in visited and visited[current]<curr_p:return
            visited[current] = min(visited.get(current,mmxx),curr_p)

            for i,p in fl.get(current,[]):
                
                fly(i,curr_p+p,stops+1)
            return 
        mmxx = 0
        for f,t,p in flights:
            if f not in fl:
                fl[f]=[]
            fl[f].append([t,p])
            mmxx+=p

        visited = {dst:mmxx}
        # print(fl)
            
        fly(src,0,0)
        return -1 if visited[dst] == mmxx else visited[dst]