class Solution:
    def getSum(self, a: int, b: int) -> int:

        carry = 0

        sums = 0
        
        for i in range(32):
            a_last = (a >> i) & 1
            b_last = (b >> i) & 1

            count = 0

            if carry == 1:
                count += 1
            if a_last == 1:
                count += 1
            if b_last == 1:
                count += 1

            carry = count >> 1
            bit = count & 1

            sums = sums | (bit << i)

        if sums > 0x7FFFFFFF:
            sums = ~(sums ^ 0xFFFFFFFF)
        
        return sums

        carry = 0

        sums = 0

        shift = 0
        
        while a != 0 or b != 0 or carry != 0:
            a_last = a & 1
            b_last = b & 1

            count = 0

            if carry == 1:
                count += 1
            if a_last == 1:
                count += 1
            if b_last == 1:
                count += 1

            carry = count >> 1
            bit = count & 1

            sums = sums << 1
            sums = sums ^ bit

            a = a >> 1
            b = b >> 1

            shift += 1

        output = 0

        for i in range(32):
            output = output << 1

            if 32 - i > shift:
                continue

            bit = sums & 1

            output = output ^ bit

            sums = sums >> 1
        
        return output
