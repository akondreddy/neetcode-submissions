class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Solution 2: Use slow and fast pointer to find
        # a cycle

        slow, fast = 0, 0
        while True:
            # Traverse to next node
            slow = nums[slow]
            # Traverse two nodes
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        