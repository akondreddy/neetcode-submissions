# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Keep a pointer in order to determine which list to add from
        node = ListNode()
        # This will be the start of the linked list
        start = node
        # While both list1 and list2 have values in them
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            # Move to the next node, continuously adding
            node = node.next
        # Once one list is finished, add the remainder of the other list,
        # if it's there
        node.next = list1 or list2
        # Return the linked list from the start of the list
        return start.next