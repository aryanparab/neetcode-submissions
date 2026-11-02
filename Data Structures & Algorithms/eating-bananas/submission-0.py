class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)>h:return -1
        if len(piles)==h:return max(piles)
        highest = max(piles)
        lowest = 1
        ans = highest
        while highest>=lowest:
            new_val = (highest+lowest)//2
            hs=0
            for i in piles:
                hs += math.ceil(float(i) / new_val)
            if hs<=h:
                ans = new_val
                highest=new_val-1
            else:
                lowest = new_val+1
        return ans


            
