class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), key=lambda i:i[0], reverse=True)
        
        stack = []

        for pos, spe in cars:
            time = (target - pos) / spe

            if stack and stack[-1] >= time:
                continue

            stack.append(time)

        return len(stack)
