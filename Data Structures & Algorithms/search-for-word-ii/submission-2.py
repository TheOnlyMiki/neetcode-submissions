class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        tree_head = {}
        
        def prefixTreeInsert(node, word):
            for c in word:
                if c not in node:
                    node[c] = {}
                
                node = node[c]

            node['#'] = word

        for word in words:
            prefixTreeInsert(tree_head, word)

        m, n = len(board), len(board[0])

        def dfs(i, j, node):
            if 0 <= i < m and 0 <= j < n and board[i][j] != '.' and board[i][j] in node:
                c = board[i][j]
                board[i][j] = '.'

                if '#' in node[c]:
                    output.append(node[c]['#'])
                    del node[c]['#']

                for a, b in [(1,0), (0, 1), (-1, 0), (0, -1)]:
                    dfs(i+a, j+b, node[c])

                board[i][j] = c

                if not node[c]:
                    del node[c]

            return

        output = []

        for i in range(m):
            for j in range(n):
                dfs(i, j, tree_head)

        return output
            