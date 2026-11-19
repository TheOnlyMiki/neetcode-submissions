class Solution:
    def reverseBits(self, n: int) -> int:

        bits = 0

        output=[]
        
        for i in range(32):

            bits = bits << 1

            have_one = n & 1
            bits = bits ^ have_one
            
            n = n >> 1

        return bits

            
