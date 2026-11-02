class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ss = []
        def trav(i,curr):
            if len(curr)==k:
                ss.append(curr.copy())
                return 
            if i==n+1:return 
            curr.append(i)
            trav(i+1,curr)
            curr.pop()
            trav(i+1,curr)
            return
        trav(1,[])
        return ss