class KthLargest:
    # First solution
    # Every time a new element is added,
    # sort the list then just pick the len - k
    # index for the largest
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums = sorted(self.nums)
        return self.nums[len(self.nums) - self.k]
