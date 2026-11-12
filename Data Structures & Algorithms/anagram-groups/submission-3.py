class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        record = defaultdict(list)

        # Method 1
        """
        for word in strs:
            temp = "".join(sorted(word))
            '''
            if temp in record:
                record[temp].append(word)
            else:
                record[temp] = [word]'''
            #record[temp] = record.get(temp, []) + [word]

            record[temp].append(word)
        """
        # time complexity O(n nlogn), space complexity O(n m)

        # Method 2
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1

            record[tuple(count)].append(word)

        return list(record.values())