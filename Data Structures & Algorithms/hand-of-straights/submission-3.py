class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
        
        record = defaultdict(int)
        for num in hand:
            record[num] += 1

        hand.sort()

        for num in hand:
            if record[num] == 0:
                continue

            for i in range(num, num + groupSize):
                if record[i] == 0:
                    return False

                record[i] -= 1

        return True

        if len(hand) % groupSize != 0:
            return False
        
        record = {}

        start = float('inf')

        for num in hand:
            if num not in record:
                record[num] = 0

            record[num] += 1
            start = min(start, num)

        group_current_size = 0

        while record:
            if start not in record:
                return False

            record[start] -= 1

            if record[start] == 0:
                del record[start]

            group_current_size += 1
            if group_current_size == groupSize:
                group_current_size = 0

                start = float('inf')
                for num in record.keys():
                    start = min(start, num)
            else:
                start += 1

        return True
