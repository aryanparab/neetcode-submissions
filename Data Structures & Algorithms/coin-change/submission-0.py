class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = 0
        coins.sort()
        coins = coins[::-1]
        for coin in coins:
            if coin>amount:continue
            # print(coin,amount,ans)
            r = amount%coin
            ans += amount//coin
            amount = r
            # print(coin,amount,ans)
            if r==0:
                break
        # print(amount,ans)
        if amount !=0:return -1
        return ans
                