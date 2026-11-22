class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = []
        for i in queries:
            res = float('inf')
            for j,k in intervals:
                if j<= i and  i<=k:
                    res = min(res,k-j+1)
            if res==float('inf'):
                ans.append(-1)
            else:
                ans.append(res)
        return ans
                    