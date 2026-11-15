class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}
        
        def dfs(i, j):
            if j >= len(prices):
                return 0

            if (i, j) in dp:
                return dp[(i,j)]

            profit = prices[j] - prices[i]
            if profit > 0:
                dp[(i,j)] = max(profit + dfs(j+2, j+3), dfs(i, j+1))
            else:
                dp[(i,j)] = max(0, dfs(i+1, i+2))
            
            return dp[(i,j)]

        return dfs(0, 1)
