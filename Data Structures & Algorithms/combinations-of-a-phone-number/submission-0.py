class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        output = []

        maps = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtrack(i, path):

            if len(path) == len(digits):
                output.append("".join(path))
                return

            for c in maps[digits[i]]:
                path.append(c)

                backtrack(i+1, path)

                path.pop()

        backtrack(0, [])

        return output