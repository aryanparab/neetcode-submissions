class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        memo = {}
        def finder(i,curr):
            if i==len(intervals):
                return 0
            x = str(curr)
            if (i,x) in memo:
                return memo[(i,x)]
            if curr[1]>intervals[i][0]:
                memo[(i,x)] =  1+ min(finder(i+1,curr),finder(i+1,intervals[i]))
            else:
                memo[(i,x)]=  finder(i+1,intervals[i])
            return memo[(i,x)]
        intervals.sort(key=lambda x : (x[0],x[1]))
     
        return finder(1, intervals[0])
         