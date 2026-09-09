class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Brute force
        # Three independent checks that will show
        # if in the row, col, or square

        for row in range(9):
            rowSet = set()
            for cell in range(9):
                value = board[row][cell]
                if value == ".":
                    continue
                if value in rowSet:
                    return False
                else:
                    rowSet.add(value)
        
        for col in range(9):
            colSet = set()
            for cell in range(9):
                value = board[cell][col]
                if value == ".":
                    continue
                if value in colSet:
                    return False
                else:
                    colSet.add(value)

        
        for square in range(9):
            squareSet = set()
            for row in range(3):
                for col in range(3):
                    curRow = (square // 3) * 3 + row
                    curCol = (square % 3) * 3 + col
                    
                    value = board[curRow][curCol]
                    if value == ".":
                        continue
                    if value in squareSet:
                        return False
                    else:
                        squareSet.add(value)

        return True