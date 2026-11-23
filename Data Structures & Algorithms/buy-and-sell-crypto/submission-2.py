class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        pre_low = prices[0]

        for i in range(1, len(prices)):
            if prices[i] - pre_low > profit:
                profit = prices[i] - pre_low

            pre_low = min(pre_low, prices[i])
            
        return profit
