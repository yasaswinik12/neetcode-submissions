# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        middle = slow
        prev = None
        while middle:
            next_node = middle.next
            middle.next = prev
            prev = middle
            middle = next_node
        left = head
        right = prev
        res = 0
        while right:
            twin_sum = left.val + right.val
            res = max(res, twin_sum)
            left=left.next
            right = right.next
        return res

            

        
