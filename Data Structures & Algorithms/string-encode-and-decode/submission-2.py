class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for s in strs:
            output = output + str(len(s)) + "#" + s

        return output

    def decode(self, s: str) -> List[str]:
        output = []

        i = 0

        while i < len(s):
            temp_i = i
            while s[temp_i] != '#':
                temp_i += 1

            length = int(s[i:temp_i])
            start_i = temp_i + 1
            end_i = start_i + length
            output.append(s[start_i:end_i])

            i = end_i

        return output
