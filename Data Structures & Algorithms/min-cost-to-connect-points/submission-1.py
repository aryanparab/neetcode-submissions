class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int: 
        
        points.sort(key = lambda x:(x[0],x[1]))
        points = [[1000000,1000000]] + points
        cost =0
    
        for i in range(2,len(points)):
          
            cost+= min(abs(points[i][0]-points[i-1][0]) + abs(points[i][1]-points[i-1][1]) , abs(points[i][0]-points[i-2][0]) + abs(points[i][1]-points[i-2][1]) )
        return cost