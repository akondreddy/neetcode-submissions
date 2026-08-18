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
        
        newHead = head
        # Divide into subproblems, use recursion...
        # If there is another node
        if head.next:
            # Set the head to the next node
            newHead = self.reverseList(head.next)
            # Move onto the next subproblem
            head.next.next = head
        # For the last node, set it to point to None
        head.next = None
        return newHead

            
        