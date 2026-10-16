# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy  = ListNode(0, head)
        left  = dummy
        Right = head
        while n > 0 and Right:
            Right = Right.next
            n -= 1
        
        while Right:
            left = left.next
            Right = Right.next
        
        left.next = left.next.next
        return dummy.next