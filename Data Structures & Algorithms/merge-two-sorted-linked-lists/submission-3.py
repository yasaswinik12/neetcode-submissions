# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        p1 = list1
        p2 = list2
        cur = ListNode()
        while p1 and p2:
            if p1.val < p2.val:
                cur.next = p1
                cur = p1
                p1 = p1.next
                if not head:
                    head = cur
            else:
                cur.next = p2
                cur = p2
                p2 = p2.next
                if not head:
                    head = cur
        if p1 and not p2:
            cur.next = p1
            if not head:
                head = cur.next
        elif p2 and not p1:
            cur.next = p2
            if not head:
                head = cur.next
        return head

        