class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        mx = 0
        while r>l:
            mx = max(mx, (r-l)*min(heights[r],heights[l]))
            if heights[r]>heights[l]:
                l+=1
            else:
                r-=1
        return mx