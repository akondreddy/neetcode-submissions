class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Another thought I have is to use DFS to avoid
        # revisiting cells we have already visited.
        # A hashset may be best for this

        path = set()
        row, col = len(board), len(board[0])

        def dfs(curRow, curCol, index):
            # Reached the end of the word, all matched
            if index == len(word):
                return True
            
            # If we are out of bounds, not equal
            # to the current char, or revisiting node,
            # then return False.
            if curRow < 0 or curCol < 0 or curRow >= row or curCol >= col or (curRow, curCol) in path or word[index] != board[curRow][curCol]:
                return False

            # Visited
            path.add((curRow, curCol))
            result = (dfs(curRow + 1, curCol, index + 1) or dfs(curRow - 1, curCol, index + 1) or dfs(curRow, curCol + 1, index + 1) or dfs(curRow, curCol - 1, index + 1))
            path.remove((curRow, curCol))
            return result

        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True

        return False



        