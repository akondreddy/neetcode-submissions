class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # In order to solve this anagram question,
        # my idea is to count just the characters in
        # the string. Match the frequency of the chars
        # in each words to each other.

        # dict to store frequencies
        anagrams = {}
        for i in range(len(strs)):
            word = strs[i]
            # dict to store chars
            frequency = [0] * 26
            for j in range(len(word)):
                char = word[j]
                frequency[ord(char) - ord("a")] += 1
            tupled = tuple(frequency)
            anagrams[tupled] = anagrams.get(tupled, []) + [word]

        return list(anagrams.values())