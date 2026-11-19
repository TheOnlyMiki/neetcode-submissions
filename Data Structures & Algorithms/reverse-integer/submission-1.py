class Solution:
    def reverse(self, x: int) -> int:

        negative = -1 if x < 0 else 1

        x = abs(x)
        
        powers = []
        record = []

        power = 1

        while x != 0:
            
            remain = x % 10

            record.append(remain)

            powers.append(power)
            power = power * 10

            x = x // 10

        output = 0

        for i in range(len(record)):
            power = powers.pop()
            output += record[i] * power

        if output > 0x7FFFFFFF:
            return 0

        output = negative * output

        return output 
