class Solution:
    profit = 0
    def maxProfit(self, prices: List[int]) -> int:
        #buy -> sell i+2
        #skip -> buy or sell
        #if profit<0 skip
        def skipy(i,flag,profit):
            if i>=len(prices):
                return profit
            if flag==0:
                a1 = skipy(i+1,1,profit-prices[i])
                a2 = skipy(i+1,flag,profit)
                return max(a1,a2)
            else:
                a1= skipy(i+2,0,profit+prices[i])
                a2 = skipy(i+1,flag,profit)
                return max(a1,a2)
        return skipy(0,0,0)