# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Brute force: 
        # Iterate, add nums at that index
        summed = ListNode()
        iterate = summed
        over = 0
        while l1 or l2 or over:
            # Ensures both l1 and l2 are valid
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            # Carry over
            total = num1 + num2 + over

            # If it goes over
            over = total // 10
            total %= 10

            iterate.next = ListNode(total)
            iterate = iterate.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return summed.next
        

