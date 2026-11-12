class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        self.n = n

        output = []

        record = { '(':n, ')':n }

        def backtrack(path, n, m):
            if n == m == self.n:
                output.append("".join(path))
                return

            if n < self.n:
                path.append('(')
                backtrack(path, n+1, m)
                path.pop()

            if m < n:
                path.append(')')
                backtrack(path, n, m+1)
                path.pop()

        backtrack([], 0, 0)

        return output