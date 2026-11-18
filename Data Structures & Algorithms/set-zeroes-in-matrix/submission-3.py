class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])
        col_0 = False
        row_0 = False

        for x in range(m):
             if matrix[x][0] == 0:
                col_0 = True
                break
        for y in range(n):
            if matrix[0][y] == 0:
                row_0 = True
                break

        for x in range(1, m):
            for y in range(1, n):
                if matrix[x][y] == 0:
                    matrix[x][0] = 0
                    matrix[0][y] = 0

        for x in range(1, m):
            for y in range(1, n):
                if matrix[x][0] == 0 or matrix[0][y] == 0:
                    matrix[x][y] = 0

        if col_0:
            for x in range(m):
                matrix[x][0] = 0

        if row_0:
            for y in range(n):
                matrix[0][y] = 0

        return


        m, n = len(matrix), len(matrix[0])
        
        row = set()
        col = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j] = 0

        return