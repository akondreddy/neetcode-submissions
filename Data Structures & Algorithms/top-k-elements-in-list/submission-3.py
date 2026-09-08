class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a minheap to keep track of only the 
        # k most frequent items in nums
        frequency = {}
        for i in range(len(nums)):
            num = nums[i]
            frequency[num] = frequency.get(num, 0) + 1
        
        minHeap = []

        # Push the num onto the heap.
        # If the length of the heap exceeds k,
        # pop once to remove the smallest frequency
        for num, count in frequency.items():
            heapq.heappush(minHeap, [count, num])
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        answer = []
        while len(minHeap) > 0:
            answer.append(heapq.heappop(minHeap)[1])

        return answer
            