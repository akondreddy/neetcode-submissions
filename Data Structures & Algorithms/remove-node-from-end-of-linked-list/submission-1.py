# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # First find the length of the ListNode
        # From there, length - n is the node to remove
        
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        remainder = length - n
        # If we want to remove the first element
        if remainder == 0:
            return head.next
        
        current = head
        for i in range(length - 1):
            if (i + 1) == remainder:
                current.next = current.next.next
                break
            current = current.next
        return head