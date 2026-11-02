class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][1]<temperatures[i]:
                
                x,y=stack.pop(-1)
                ans[x] = i-x
            
            stack.append([i,temperatures[i]])
        return ans

