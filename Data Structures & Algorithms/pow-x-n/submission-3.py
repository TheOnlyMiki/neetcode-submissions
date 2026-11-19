class Solution:
    def myPow(self, x: float, n: int) -> float:

        if x == 0 or x == 1:
            return x
        
        def dfs(x, power):
            if power == 0:
                return 1

            result = dfs(x*x, power//2)

            return x * result if power % 2 == 1 else result

        result = dfs(x, abs(n))

        return result if n >= 0 else 1.0 / result