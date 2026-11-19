class Solution:
    def myPow(self, x: float, n: int) -> float:

        if x == 0 or x == 1:
            return x
        
        def dfs(x, power):
            if power == 0:
                return 1

            # 递归计算一半的幂次
            result = dfs(x * x, power // 2)
            
            # 如果当前幂次是奇数，需要额外乘一个当前的 x
            if power % 2 == 1:
                return x * result
                
            return result

        result = dfs(x, abs(n))

        return result if n >= 0 else 1.0 / result