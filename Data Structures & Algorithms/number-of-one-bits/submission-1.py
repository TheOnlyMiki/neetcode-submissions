class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0

        while n != 0:
            remain_one = n & 1

            count += remain_one

            n = n >> 1

        return count
        
        count = 0

        while n != 0:
            
            remain_one = n % 2

            count += remain_one

            n = n // 2

        return count