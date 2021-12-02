class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # O(9)
        def checkValidity(line):
            numbers = set([x for x in range(1, 10)])
            try:
                for i in line:
                    if i != ".":
                        numbers.remove(int(i))
            except:
                return False
            return True
        
        
        # check rows, O(9)
        for row in board:
            if not checkValidity(row):
                return False
        
        # make columns, O(9*9)
        columns = []
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            columns.append(column)
        # check columns, O(9)
        for column in columns:
            if not checkValidity(column):
                return False
        
        # make boxes
        boxes = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []
                box.append(board[i][j])
                box.append(board[i+1][j])
                box.append(board[i+2][j])
                box.append(board[i][j+1])
                box.append(board[i+1][j+1])
                box.append(board[i+2][j+1])
                box.append(board[i][j+2])
                box.append(board[i+1][j+2])
                box.append(board[i+2][j+2])
                boxes.append(box)
        # check boxes, O(9)
        for box in boxes:
            if not checkValidity(box):
                return False
        
        return True