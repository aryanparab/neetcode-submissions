import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        reaches =[]
        n = len(position)
        x = [[position[i],speed[i]] for i in range(n)]
        x.sort(key=lambda y:(-y[0],y[1]))
        
        for i in range(n):
            j = math.ceil((target-x[i][0])/x[i][1])
            reaches.append(j)
        fleet = 1
        for i in range(1,n):
            if reaches[i]>reaches[i-1]:
                fleet+=1
        return fleet
        
