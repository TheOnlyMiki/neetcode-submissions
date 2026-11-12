class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Method 1 - stack
        '''cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for pos, speed in cars:
            time = (target - pos) / speed

            if stack and time <= stack[-1]:
                continue

            stack.append(time)

        return len(stack)'''
        # time complexity O(nlogn), space complexity O(n)

        # Method 2 
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 1
        pre_time = (target - cars[0][0]) / cars[0][1]

        for i in range(1, len(position)):
            cur_time = (target - cars[i][0]) / cars[i][1]
            if cur_time > pre_time:
                fleets += 1
                pre_time = cur_time

        return fleets
