import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        dt = {}
        for i in range(len(s)):
            dt[s[i]] = dt.get(s[i],0)+1
        hp =[]

        for i,j in dt.items():
            heapq.heappush(hp,(-1*j,i))
       
        ans = ""
        while hp:
            
            x,y = heapq.heappop(hp)
            
            if ans!="" and ans[-1]==y :
                if not hp:return ""
                dx,dy = heapq.heappop(hp)
                ans+=dy
                if dx+1!=0:
                    heapq.heappush(hp,(dx+1,dy))
                heapq.heappush(hp,(x,y))
            else:
                ans+=y
                if x+1!=0:
                    heapq.heappush(hp,(x+1,y))
        return ans