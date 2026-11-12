class MinStack:
    # Method 1 - 两个stack，其中一个存当前最小值
    '''def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else -1

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else -1
    # time complexity O(1), space complexity O(2 n)
'''
    #Method 2 - 一个stack 存 差值
    def __init__(self):
        self.stack = []
        self.min_val = float("inf")

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_val = val
        else:
            self.stack.append(val - self.min_val)
            if self.min_val > val:
                self.min_val = val

    def pop(self) -> None:
        cur = self.stack.pop()
        # 如果当前数字就是最小的，比其他数小的话差值一定是负数
        if cur < 0:
            self.min_val = self.min_val - cur

    def top(self) -> int:
        cur = self.stack[-1]
        # 如果当前数字就是最小的，比其他数小的话差值一定是负数
        if cur <= 0:
            return self.min_val
        else: # 否则就是差值+最小数=当前
            return cur + self.min_val

    def getMin(self) -> int:
        return self.min_val