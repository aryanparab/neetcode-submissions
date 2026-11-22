class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        coins.sort()
        coins = coins[::-1]
        def pick(amt, res):
           
            if amt ==0:
                return res
            if amt<0:
                return float('inf')
            # if amt in memo and memo[amt]:
            
            mn = float('inf')
            for coin in coins:
                x = pick(amt-coin,res+1)
                mn = min(x,mn)
            memo[amt]=mn
            return memo[amt]
        v = pick(amount,0)
        return -1 if v == float('inf') else v
