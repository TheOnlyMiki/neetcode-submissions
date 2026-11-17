class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(m):
            for j in range(n // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n-1-j]
                matrix[i][n-1-j] = temp

        return