class Solution:
    ans = float('inf')
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dd = set(dictionary)

        def trav(ss,pending,i):
            if i==len(s):
                self.ans =min(self.ans,pending)
                return
            if ss in dd:
                trav("",pending-len(ss)+1,i+1)
            trav(ss+s[i],pending+1,i+1)
            trav("",pending+1,i+1)
            return 
        trav("",0,0)
        return self.ans
            

