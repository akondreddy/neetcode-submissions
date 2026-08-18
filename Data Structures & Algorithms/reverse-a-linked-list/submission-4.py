# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If empty
        if not head:
            return None
        previous, current = None, head
        
        # Reverse the linked list by getting current,
        # then setting temp value for the next value.
        # The current node should point to the one
        # before it, then the previous node becomes
        # the current one, then we iterate to the next
        # node.
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        return previous
            
        