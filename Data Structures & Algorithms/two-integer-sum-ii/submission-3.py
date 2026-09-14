class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Brute force, loop through
        # with hashmap and then check if the difference
        # is in the map

        within = {}
        for i in range(len(numbers)):
            within[numbers[i]] = i
        
        for i in range(len(numbers)):
            remainder = target - numbers[i]
            if remainder in within and within[remainder] != i:
                return [i + 1, within[remainder] + 1]
        
        return []


        