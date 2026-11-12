class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), reverse=True)

        output = 0

        stack = []

        for pos, speed in cars:
            time = (target - pos) / speed

            if stack and time <= stack[-1]:
                continue

            stack.append(time)

        return len(stack)