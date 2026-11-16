from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = {}

        #@cache
        def dfs(i: int, holding: bool) -> int:
            # 小提示：卖出后会跳到 i+2，可能直接越界，所以必须是 >= 不是 ==
            if i >= n:
                return 0

            if (i, holding) in dp:
                return dp[(i, holding)]

            skip = dfs(i + 1, holding)            # 今天什么都不做

            if holding:
                # 卖出：+prices[i]，并跳过冷冻期 i+1
                sell = prices[i] + dfs(i + 2, False)
                dp[(i, holding)] = max(skip, sell)
            else:
                # 买入：-prices[i]，明天就是持股状态
                buy = -prices[i] + dfs(i + 1, True)
                dp[(i, holding)] = max(skip, buy)

            return dp[(i, holding)]

        return dfs(0, False)

# 时间 O(n)：状态数为 n × 2，每个状态 O(1)
# 空间 O(n)：memo 加上递归栈
# 小提示：不加 @cache 的话是 O(2^n)，一定超时；加上之后每个 (i, holding) 只算一次
# 小提示：Python 默认递归深度限制在 1000 左右，本题 n ≤ 5000，
#        如果本地运行报 RecursionError，在开头加 sys.setrecursionlimit(10**4)
#        （LeetCode 平台上一般不会报这个错）

        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i+1, buying)

            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return dfs(0, True)
            
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
                dp[(i,j)] = dfs(i+1, i+2)
            
            return dp[(i,j)]

        return dfs(0, 1)
