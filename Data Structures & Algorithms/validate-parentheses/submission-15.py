class Solution:
    def isValid(self, s: str) -> bool:

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
        