class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        def check_valid(c):
            return (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z')) or (ord('0') <= ord(c) <= ord('9'))
            
        while left < right:
            while left < right and not check_valid(s[left]):
                left += 1

            while left < right and not check_valid(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left, right = left+1, right-1

        return True
    # time complexity O(n), space compxity O(1)