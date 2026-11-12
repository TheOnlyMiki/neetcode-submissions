class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Method 1 - two pointer
        '''left, right = 0, len(s)-1

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

        return True'''

        l, r = 0, len(s)-1
        while l <= r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[r].lower() != s[l].lower():
                return False
            r-=1
            l+=1

        return True
        # time complexity O(n), space compxity O(1)

        # Method 2 - reverse
        '''new_s = ''
        for c in s:
            if c.isalnum():
                new_s += c.lower()

        return new_s == new_s[::-1]'''
        # time complexity O(n), space complexity O(n)
