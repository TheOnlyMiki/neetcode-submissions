class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # Method 1 

        # Stack 反方向
        '''stack = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                output[i] = stack[-1] - i
            else:
                output[i] = 0
                
            stack.append(i)

        return output
        # time complexity O(n), space complexity O(n)

        # Stack 正方向
        stack = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pre_i = stack.pop()
                output[pre_i] = i - pre_i
                
            stack.append(i)

        return output'''
        # time complexity O(n), space complexity O(n)

        # Method 2 
        # Dynamic Program - space O(1)
        n = len(temperatures)
        output = [0] * n

        for i in range(n-2, -1, -1):
            next_i = i + 1
            while next_i < n and temperatures[i] >= temperatures[next_i]:
                if output[next_i] == 0:
                    next_i = n
                    break
                next_i = next_i + output[next_i]

            if next_i < n:
                output[i] = next_i - i

        return output
