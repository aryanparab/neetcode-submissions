class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        coins.sort()
        coins = coins[::-1]
        def pick(amt):
           
            if amt ==0:
                return 0
            if amt<0:
                return float('inf')
            if amt in memo :
                return memo[amt]
            mn = float('inf')
            for coin in coins:
                x = 1 + pick(amt-coin)
                mn = min(x,mn)
            memo[amt]=mn
            return memo[amt]
        v = pick(amount)
        return -1 if v == float('inf') else v
