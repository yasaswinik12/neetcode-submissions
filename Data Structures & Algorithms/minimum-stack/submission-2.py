class MinStack:

    def __init__(self):
        self.stack = []
        self.track_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.track_min:
            self.track_min = [val]
        elif val <= self.track_min[-1]:
            self.track_min.append(val)

    def pop(self) -> None:
        popped_ele = self.stack[-1]
        self.stack.pop()
        if self.track_min[-1]==popped_ele:
            self.track_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.track_min[-1]

        
