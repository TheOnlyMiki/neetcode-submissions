class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = {}

        for word in strs:
            temp = "".join(sorted(word))
            if temp in record:
                record[temp].append(word)
            else:
                record[temp] = [word]
            #record[temp] = record.get(temp, []) + [word]

        return list(record.values())