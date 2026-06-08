class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(num):
            if num == 0:
                return 0
            if num in dp:
               return dp[num] 

            res = float('inf')
            for coin in coins:
                if num - coin >= 0:
                    res = min(res, 1 + dfs(num - coin))

            dp[num] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins == float('inf') else int(minCoins)

