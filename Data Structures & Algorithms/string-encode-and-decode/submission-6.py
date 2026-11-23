class Solution:
    
    def encode(self, strs: List[str]) -> str:
        
        output = ""

        for s in strs:
            output += str(len(s)) + '#' + s

        return output

    def decode(self, s: str) -> List[str]:

        i = 0
        output = []

        while i < len(s):
            
            temp_i = i

            while s[temp_i] != '#':
                temp_i += 1

            length = int(s[i:temp_i])
            start = temp_i + 1
            end = start + length

            output.append(s[start:end])
            
            i = end

        return output
