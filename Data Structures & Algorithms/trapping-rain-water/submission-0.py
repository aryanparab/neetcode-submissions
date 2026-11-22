class Solution:
    def trap(self, height: List[int]) -> int:
        current_max = [height[0],0]
        trapped = 0
        
        for i in range(1,len(height)):
            if height[i]>=current_max[0]:
                ht = min(current_max[0],height[i])
                
                for k in range(i-1,current_max[1],-1):
                    trapped+=(ht-height[k])
                current_max = [height[i],i]
        return trapped