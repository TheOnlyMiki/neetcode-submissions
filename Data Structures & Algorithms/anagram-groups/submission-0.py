class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = {}

        for word in strs:
            temp = "".join(sorted(word))
            if temp in record:
                record[temp].append(word)
            else:
                record[temp] = [word]

        return [ value for value in record.values() ]