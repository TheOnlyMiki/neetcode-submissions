class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        table = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        for c in s:
            if c in table:
                if stack and table[c] == stack.pop():
                    continue
                return False
            else:
                stack.append(c)

        return len(stack) == 0