class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # An important aspect of this problem
        # is checking for duplicates.
        # hashsets would be best for this.

        # Now, how to check each square? 
        # Nested for loop?

        # Hashsets for the rows, columns, and squares
        # 27 sets, 3 lists
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        squareSet = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                # Ignore empty cells
                if cell == ".":
                    continue
                if cell in rowSet[row] or cell in colSet[col] or cell in squareSet[(row // 3) * 3 + (col // 3)]:
                    return False
                else:
                    rowSet[row].add(cell)
                    colSet[col].add(cell)
                    squareSet[(row // 3) * 3 + (col // 3)].add(cell)
        
        return True
            
