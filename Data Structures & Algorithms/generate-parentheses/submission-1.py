class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        output = []

        def backtrack(path, open_count, close_count):
            if open_count == close_count == n:
                output.append("".join(path))
                return

            if open_count < n:
                path.append('(')
                backtrack(path, open_count+1, close_count)
                path.pop()

            if close_count < open_count:
                path.append(')')
                backtrack(path, open_count, close_count+1)
                path.pop()

        backtrack([], 0, 0)

        return output