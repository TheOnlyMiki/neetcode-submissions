class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        cols = set()
        diag = set()
        reverse_diag = set()

        output = []

        def dfs(row, path):
            if len(path) == n:
                output.append(path[:])
                return

            for col in range(n):
                if col in cols or row + col in diag or row - col in reverse_diag:
                    continue

                cols.add(col)
                diag.add(row + col)
                reverse_diag.add(row - col)

                path.append('.' * col + 'Q' + '.' * (n - col - 1))

                dfs(row+1, path)

                path.pop()
            
                cols.remove(col)
                diag.remove(row + col)
                reverse_diag.remove(row - col)

        dfs(0, [])

        return output