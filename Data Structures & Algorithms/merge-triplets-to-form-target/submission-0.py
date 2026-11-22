class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #check if it is possible for 7 , 2 and 3 to be largest in their respective position 
        mxs = [0,0,0]
        for trip in triplets:
            for i in range(3):
                mxs[i] = max(mxs[i],trip[i])
        if mxs == target:return True
        return False