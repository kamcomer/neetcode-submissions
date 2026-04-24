class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] <= prices[left]:
                left = i

            res = max(res, prices[i] - prices[left])

        return res            
