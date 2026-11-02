import math

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_least_wt = max(weights)
        x1 =sum(weights)/days
        if  x1< float(min_least_wt):
            return min_least_wt
        min_least_wt = math.ceil(x1)
        while True:
            tdays = 1
            curr_sum = 0
            for i in weights:
                if curr_sum+i <= min_least_wt:
                    curr_sum+=i
                else:
                    curr_sum=i
                    tdays+=1
                
            if tdays>days:
                min_least_wt+=1
            else:
                return min_least_wt

