class Solution:
    ans = 0
    def maxProfit(self, prices: List[int]) -> int:
        
        mxp = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                mxp+=prices[i]-prices[i-1]
        return mxp