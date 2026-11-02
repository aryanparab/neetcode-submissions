class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        temp = [intervals[0]]
        for i in range(1,len(intervals)):
            if temp[-1][1]>=intervals[i][0]:
                last = temp.pop(-1)
                last= [last[0],max(last[1],intervals[i][1])]
                temp.append(last)
            
            else:
                temp.append(intervals[i])
        return temp