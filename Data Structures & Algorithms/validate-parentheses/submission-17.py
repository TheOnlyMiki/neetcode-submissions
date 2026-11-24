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
        # time complexity O(n), space complexity O(n)

        stack = []

        for c in s:
            if c == ']':
                if not stack:
                    return False

                if stack.pop() != '[':
                    return False

            elif c == ')':
                if not stack:
                    return False

                if stack.pop() != '(':
                    return False

            elif c == '}':
                if not stack:
                    return False

                if stack.pop() != '{':
                    return False

            else:
                stack.append(c)

        return False if stack else True
        