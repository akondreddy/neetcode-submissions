class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Could use a max-heap to keep max element 
        # at the top
        heap = []
        for x, y in points:
            # We want to remove the largest ones
            distance = -((x)**2 + (y)**2)
            heapq.heappush(heap, [distance, x, y])
            if len(heap) > k:
                # Pop removes and returns the 
                # smallest value so we want to pop
                # the smallest negatives, ie, the
                # biggest when positive
                heapq.heappop(heap)
            
        result = []
        while heap:
            distance, x, y = heapq.heappop(heap)
            result.append([x, y])
        return result
