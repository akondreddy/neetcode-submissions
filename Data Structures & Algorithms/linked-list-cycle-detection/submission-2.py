# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Use the method of a slow pointer and a fast 
        # pointer, where the slow one moves one node
        # at a time, the fast moves at two nodes at a
        # time.
        # If the linked list has a cycle,
        # then at some point, the fast and slow pointer
        # will point to the same node. Otherwise, the
        # fast pointer will reach the end and return
        # False.
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

        
        
        