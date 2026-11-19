class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m, n = len(matrix), len(matrix[0])
        total = m * n

        l, r = 0, n-1
        top, bottom = 0, m-1

        output = []

        direct = 0

        while len(output) < total:
            direct = direct % 4

            if direct == 0:
                output += matrix[top][l : r+1]

                top += 1

            elif direct == 1:
                
                for i in range(top, bottom+1):
                    output.append(matrix[i][r])

                r -= 1

            elif direct == 2:

                for i in range(r, l-1, -1):
                    output.append(matrix[bottom][i])

                bottom -= 1

            else:

                for i in range(bottom, top -1, -1):
                    output.append(matrix[i][l])

                l += 1

            direct += 1

        return output

        m, n = len(matrix), len(matrix[0])

        total = m * n

        output = []
        left, right = 0, n
        top, bottom = 0, m

        while len(output) < total:
            for i in range(left, right):
                output.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                output.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break
            
            for i in range(right - 1, left - 1, -1):
                output.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                output.append(matrix[i][left])
            left += 1

        return output

