class KthLargest:
    # Use a min heap
    # Add to the heap, if the number of elements
    # in the heap exceeds k, then remove elements.
    # This way, the element that we return will be 
    # the kth largest integer
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) 
        return self.minHeap[0]
        
