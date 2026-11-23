class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s)-1

        def check(c):
            num = ord(c)
            if ord('a') <= num <= ord('z') or ord('A') <= num <= ord('Z') or ord('0') <= num <= ord('9'):
                return True

            return False

        while l < r:
            
            while l < r and not check(s[l]):
                l += 1

            while l < r and not check(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

            
