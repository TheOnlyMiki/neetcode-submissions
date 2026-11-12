class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Method 1 - time complexity O(n), space complexity O(s+t)
        '''
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        return count_s == count_t'''

        # Method 2 - time complexity O(n logn), space complexity O(1) or O(s+t)
        '''return sorted(s) == sorted(t)
        '''

        # Method 3 - time complexity O(n + m), space complexity O(1)
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for n in count:
            if n != 0:
                return False
        return True