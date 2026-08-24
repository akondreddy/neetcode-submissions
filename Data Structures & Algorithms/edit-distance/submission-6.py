class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        memoized = {}
        def dfs(idx1, idx2):
            # Need to add in order to get to word2
            if idx1 == len1:
                return len2 - idx2
            # Need to remove in order to get word2
            if idx2 == len2:
                return len1 - idx1
            if (idx1, idx2) in memoized:
                return memoized[(idx1, idx2)]
            if word1[idx1] == word2[idx2]:
                memoized[(idx1, idx2)] = dfs(idx1 + 1, idx2 + 1)
            else:
                result = min(dfs(idx1 + 1, idx2), dfs(idx1, idx2 + 1), dfs(idx1 + 1, idx2 + 1))
                memoized[(idx1, idx2)] = result + 1
            return memoized[(idx1, idx2)]
        return dfs(0, 0)