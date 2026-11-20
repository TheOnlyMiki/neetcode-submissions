class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])

        # 出度 = 比自己大的邻居个数
        out = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x, y = i + a, j + b
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        out[i][j] += 1

        # 小提示：出度为 0 的是局部最大值，也就是所有递增路径的终点
        level = []
        for i in range(m):
            for j in range(n):
                if out[i][j] == 0:
                    level.append((i, j))

        layers = 0

        while level:
            next_level = []
            layers += 1

            for i, j in level:  # 小提示：一次处理完整一层，层数才是路径长度

                for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x, y = i + a, j + b
                    # 反着走：找比当前小的邻居，它少了一个"更大的后继"
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] < matrix[i][j]:
                        out[x][y] -= 1
                        if out[x][y] == 0:
                            next_level.append((x, y))

            level = next_level
            
        return layers
        # 小提示：复杂度同样是 O(mn)，没有递归，不会爆栈

        m, n = len(matrix), len(matrix[0])

        dp = {}
        
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i,j)]

            dp[(i,j)] = 1

            for a,b in [(1,0), (0,1), (-1,0), (0,-1)]:
                x,y = i+a, j+b

                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    dp[(i,j)] = max(dp[(i,j)], 1 + dfs(x,y))

            return dp[(i,j)]

        for i in range(m):
            for j in range(n):
                dfs(i, j)

        return max(dp.values())