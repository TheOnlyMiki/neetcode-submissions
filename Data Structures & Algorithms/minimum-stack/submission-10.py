class MinStack:

    def __init__(self):
        self.stack = []
        self.min_record = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min_record:
            self.min_record.append(min(self.min_record[-1], val))
        else:
            self.min_record.append(val)

    def pop(self) -> None:
        if self.stack and self.min_record:
            self.stack.pop()
            self.min_record.pop()

        return

    def top(self) -> int:
        return self.stack[-1] if self.stack else -1

    def getMin(self) -> int:
        return self.min_record[-1] if self.min_record else -1
