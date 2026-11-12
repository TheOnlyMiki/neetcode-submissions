class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m*n-1

        while left <= right:
            mid = (left + right) // 2

            mid_i, mid_j = mid // n, mid % n

            if matrix[mid_i][mid_j] < target:
                left = mid + 1
            elif matrix[mid_i][mid_j] > target:
                right = mid - 1
            else:
                return True

        return False

        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m*n-1

        while left <= right:
            mid = (left + right) // 2

            i = mid // n
            j = mid % n # mid - i * n

            if matrix[i][j] < target:
                left = mid + 1
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                return True

        return False