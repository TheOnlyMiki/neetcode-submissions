class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        
        l, r = 0, 0

        output = 0

        window = set()

        while r < n:

            if s[r] not in window:
                window.add(s[r])
                output = max(output, r-l+1)
                r += 1
            else:
                window.remove(s[l])
                l += 1

        return output
