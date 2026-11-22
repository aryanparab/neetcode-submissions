class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:(x[0],x[1]))
        cost =0
        for i in range(len(points)-1):
            cost+= abs(points[i+1][0]-points[i][0]) + abs(points[i+1][1]-points[i][1])
        return cost