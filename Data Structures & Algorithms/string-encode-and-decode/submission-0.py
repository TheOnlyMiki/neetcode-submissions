class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s

        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            temp_i = i
            while s[temp_i] != '#':
                temp_i += 1

            n = int(s[i:temp_i])
            start_i = temp_i + 1
            end_i = start_i + n
            output.append(s[start_i:start_i+n])
            
            i = end_i

        return output
