# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        def reverse_node(cur, prev):
            if cur is None:
                return prev
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            return reverse_node(cur, prev)
        return reverse_node(cur, prev)