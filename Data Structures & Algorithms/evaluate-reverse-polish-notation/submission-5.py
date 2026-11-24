class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for item in tokens:
            if item == '+':
                num2 = stack.pop()
                num1 = stack.pop()

                stack.append(int(num1) + int(num2))
            elif item == '-':
                num2 = stack.pop()
                num1 = stack.pop()

                stack.append(int(num1) - int(num2))
            elif item == '*':
                num2 = stack.pop()
                num1 = stack.pop()

                stack.append(int(num1) * int(num2))
            elif item == '/':
                num2 = stack.pop()
                num1 = stack.pop()

                stack.append(int(int(num1) / int(num2)))
            else:
                stack.append(int(item))

        return stack[-1]
        
        stack = []

        for c in tokens:
            if c in "+-*/":
                num1, num2 = stack.pop(), stack.pop()

                if c == '+':
                    stack.append(num2 + num1)

                elif c == '-':
                    stack.append(num2 - num1)

                elif c == '*':
                    stack.append(num2 * num1)

                else:
                    stack.append(int(num2 / num1))

            else:
                stack.append(int(c))

        return stack[0]
