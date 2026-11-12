class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # Backtrack with change in board

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

        # Backtrack with visited array

        ROWS, COLS = len(board), len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or visited[r][c]):
                return False

            visited[r][c] = True
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            visited[r][c] = False
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

        # Hash Table

        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
