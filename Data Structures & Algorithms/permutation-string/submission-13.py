class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count_s1 = [0] * 26
        window = [0] * 26

        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        match = 0
        for i in range(26):
            if count_s1[i] == window[i]:
                match += 1

        if match == 26:
            return True

        for i in range(len(s1), len(s2)):

            left_c_i = ord(s2[i-len(s1)]) - ord('a')
            window[left_c_i] -= 1
            if window[left_c_i] == count_s1[left_c_i]:
                match += 1
            elif window[left_c_i] == count_s1[left_c_i] - 1:
                match -= 1

            right_c_i = ord(s2[i]) - ord('a')
            window[right_c_i] += 1
            if window[right_c_i] == count_s1[right_c_i]:
                match += 1
            elif window[right_c_i] == count_s1[right_c_i] + 1:
                match -= 1

            if match == 26:
                return True

        return False
        