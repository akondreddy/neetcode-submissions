class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Brute force, loop through
        # with hashmap and then check if the difference
        # is in the map

        hashset = {}
        for i in range(len(numbers)):
            hashset[numbers[i]] = i
        
        for i in range(len(numbers)):
            remainder = target - numbers[i]
            if remainder in hashset and hashset[remainder] != i:
                return [i + 1, hashset[remainder] + 1]
        


        