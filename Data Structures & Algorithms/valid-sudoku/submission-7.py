class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                num = board[i][j]

                box_i = i // 3 * 3 + j // 3

                if num in row[i] or num in col[j] or num in box[box_i]:
                    return False

                row[i].add(num)
                col[j].add(num)
                box[box_i].add(num)
                
        return True
