class ListNode:
    def __init__(self, val: 0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.cur = self.head = self.tail = ListNode(0)
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        i = 0
        cur = self.head
        while i < index:
            cur = cur.next
            i += 1
        return cur.next.val


    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        cur_first = self.head.next
        self.head.next = node
        node.next = cur_first
        self.length += 1
        if self.length == 1:
            self.tail = node

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        cur_tail = self.tail
        cur_tail.next = node
        self.tail = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return None
        node = ListNode(val)
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            cur = self.head.next
            i = 0
            while i < index - 1:
                cur = cur.next
                i += 1
            next_node = cur.next
            cur.next = node
            node.next = next_node
            self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return None
        if index == 0:
            self.head.next = self.head.next.next
            self.length -= 1
            return None
        i = 0
        cur = self.head.next
        while i < index - 1:
            cur = cur.next
            i += 1
        if i == self.length - 2:
            self.tail = cur
        self.length -= 1
        cur.next = cur.next.next




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)