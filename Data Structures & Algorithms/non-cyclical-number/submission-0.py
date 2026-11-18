class Solution:
    def isHappy(self, n: int) -> bool:
        
        visit = set()

        while n != 1:
            if n in visit:
                return False

            visit.add(n)

            count = 0

            while n >= 10:
                remain = n % 10
                n = n // 10

                count += remain**2

            count += n**2
            n = count

        return True
