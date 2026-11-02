import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        reaches =[]
        n = len(position)
        x = [[position[i],speed[i]] for i in range(n)]
        x.sort(key=lambda y:(-y[0],y[1]))
        
        for i in range(n):
            j = (target-x[i][0])/x[i][1]
            reaches.append(j)
        fleet = 0
        
        i=0
        while i < n:
            current = reaches[i]
            while i+1<n and current>=reaches[i+1]:
                print(current,reaches[i+1])
                i+=1
            
            fleet+=1
            i+=1
        return fleet
        
