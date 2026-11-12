class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        matrix = defaultdict(set)

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if board[i][j] == '.':
                    continue

                # matrix_i = (i // 3, j // 3)
                matrix_i = (i // 3) * 3 + j // 3
                if cur in row[i] or cur in col[j] or cur in matrix[matrix_i]:
                    return False
                
                row[i].add(cur)
                col[j].add(cur)
                matrix[matrix_i].add(cur)

        return True
        # time complexity O(9*9 n^2), space complexity O(9*9 n^2)
                    