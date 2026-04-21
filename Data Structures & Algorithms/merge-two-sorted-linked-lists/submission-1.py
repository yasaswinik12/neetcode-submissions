# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        while list1 and list2:
            if list1.val <= list2.val:
                if head:
                    cur.next = list1
                cur = list1
                if not head:
                    head= cur
                list1 = list1.next
            else:
                if head:
                    cur.next = list2
                cur = list2
                if not head:
                    head= cur
                list2 = list2.next
        if not list1:
            if not head:
                return list2
            cur.next = list2
        else:
            if not head:
                return list1
            cur.next = list1
        return head



