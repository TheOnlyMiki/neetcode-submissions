class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        output = []

        maps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
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