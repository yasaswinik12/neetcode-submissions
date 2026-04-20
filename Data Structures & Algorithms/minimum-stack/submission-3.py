class MinStack:

    def __init__(self):
        self.stack = []
        self.min_tracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_tracker or self.min_tracker[-1] >= val:
            self.min_tracker.append(val)
        
    def pop(self) -> None:
        if self.stack:
            element = self.stack.pop()
        if self.min_tracker[-1] == element:
            self.min_tracker.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min_tracker[-1]
