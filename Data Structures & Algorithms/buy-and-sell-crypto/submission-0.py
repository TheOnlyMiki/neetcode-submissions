class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        pre_low = prices[0]

        for price in prices:
            if pre_low > price:
                pre_low = price
                continue

            cur = price - pre_low

            if profit < cur:
                profit = cur

        return profit