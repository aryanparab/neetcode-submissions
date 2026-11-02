class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def trav(i,current,ss):
            if ss==target:
                res.append(current.copy())
                return
            if ss>target or i>=len(candidates):
                return 
            current.append(candidates[i])
            trav(i+1,current,ss+candidates[i])
            current.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            trav(i+1,current,ss)
            return 
        trav(0,[],0)
        return res