class ListNode():
    def __init__(self, val:0):
        self.val = val
        self.prev = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = self.tail = self.cur = ListNode(homepage)
        self.cur_idx = 0
        self.history_len = 1

    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.cur.next = node
        node.prev = self.cur
        self.cur = node
        self.cur_idx += 1
        self.history_len = self.cur_idx + 1
        self.tail = self.cur

    def back(self, steps: int) -> str:
        if self.cur_idx - steps < 0:
            return self.head.val
        while steps:
            self.cur = self.cur.prev
            self.cur_idx -= 1
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        if self.cur_idx + steps >= self.history_len:
            return self.tail.val
        while steps:
            self.cur = self.cur.next
            self.cur_idx += 1
            steps -= 1
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)