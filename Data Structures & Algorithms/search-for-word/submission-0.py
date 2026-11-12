class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])
        
        def backtrack(i, j, word_i):
            if word_i == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            if board[i][j] != word[word_i] or board[i][j] == '#':
                return False

            board[i][j] = '#'
            
            if backtrack(i-1, j, word_i+1) or backtrack(i, j-1, word_i+1) or backtrack(i+1, j, word_i+1) or backtrack(i, j+1, word_i+1):
                return True

            board[i][j] = word[word_i]

            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
            
        return False