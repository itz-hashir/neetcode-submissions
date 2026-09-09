class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        box = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value != '.':
                    box_index = (r//3)*3+(c//3)
                    if value in row[r] or value in col[c] or value in box[box_index]:
                        return False
                    else:
                        row[r].add(value) 
                        col[c].add(value) 
                        box[box_index].add(value)
                    
        return True