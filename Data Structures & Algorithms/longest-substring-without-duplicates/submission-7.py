class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0

        window = set()
        best = 0

        for r in range(len(s)):
            
            while s[r] in window:
                window.remove(s[l])
                l += 1

            window.add(s[r])

            best = max(best, r-l+1)

        return best


















        # Method 1 - two pointer
        output = 0
        record = set()
        left = 0

        for right, c in enumerate(s):
            while c in record:
                record.remove(s[left])
                left += 1
            record.add(c)
            
            length = right - left + 1
            if length > output:
                output = length

        return output
        # time complexity O(n), space complexity O(n)