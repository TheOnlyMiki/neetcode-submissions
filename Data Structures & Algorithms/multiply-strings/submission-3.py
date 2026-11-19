class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        num1 = num1[::-1]
        num2 = num2[::-1]

        count = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            n1 = int(num1[i])

            for j in range(len(num2)):
                n2 = int(num2[j])

                result = n1 * n2

                count[i+j] += result

                count[i+j+1] = count[i+j+1] + count[i+j] // 10
                
                count[i+j] = count[i+j] % 10

        count = count[::-1]
        i = 0

        while i < len(count) and count[i] == 0:
            i += 1

        output = []

        for index in range(i, len(count)):
            output.append(str(count[index]))

        return "".join(output) if len(output) != 0 else "0"

