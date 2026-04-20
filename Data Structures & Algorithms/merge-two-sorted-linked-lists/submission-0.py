# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        while list1 != None and list2!= None:
            if list1.val <= list2.val:
                if head!=None:
                    cur.next = list1
                cur = list1
                if head==None:
                    head = cur
                list1 = list1.next
            else:
                if head!=None:
                    cur.next = list2
                cur = list2
                if head==None:
                    head = cur
                list2 = list2.next
        if list1==None:
            if head is None:
                return list2
            cur.next=list2
        else:
            if head is None:
                return list1
            cur.next=list1
        return head
