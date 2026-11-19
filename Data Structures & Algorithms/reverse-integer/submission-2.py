class Solution:
    def reverse(self, x: int) -> int:

        negative = -1 if x < 0 else 1

        x = abs(x)
        
        output = 0

        while x != 0:
            
            remain = x % 10

            output = output * 10 + remain

            if output > 0x7FFFFFFF:
                return 0

            x = x // 10

        return negative * output


