class MyStack:

    def __init__(self):
        self.stack = deque()
        self.len = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.len += 1

    def pop(self) -> int:
        counter = self.len - 1
        while counter:
            left_ele = self.stack.pop()
            self.stack.append(left_ele)
            counter -= 1
        self.len -= 1
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return self.len==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()