class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute force
        # Count the frequency of each digit
        # using a dict
        frequency = {}
        mostFrequent = []
        for i in range(len(nums)):
            num = nums[i]
            frequency[num] = frequency.get(num, 0) + 1
        
        # Now, sort the frequency by value
        for num, count in frequency.items():
            # Clever trick in which I can switch
            # the count and the number in order to 
            # find the most frequent values
            mostFrequent.append([count, num])
        # Reverse the sorted order so the most
        # frequent are at the start
        mostFrequent.sort(reverse=True)

        # mostFrequent now contains the frequencies
        # sorted.
        amount = k
        answer = []
        
        # Do only the first k most frequent
        for count, num in mostFrequent[:k]:
            answer.append(num)

        return answer