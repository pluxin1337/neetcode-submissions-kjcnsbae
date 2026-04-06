class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        temp = []
        #column check
        for j in range(9):
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in temp:
                        return False
                    else:
                        temp.append(board[i][j])
            temp = []
        
        #row check
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in temp:
                        return False
                    else:
                        temp.append(board[i][j])
            temp = []
        
        #square check
        row = 0
        column = 0
        for g in range(9):
            for i in range(3):
                for j in range(3):
                    if board[i+row][j+column] != ".":
                        if board[i+row][j+column] in temp:
                            return False
                        else:
                            temp.append(board[i+row][j+column])
            temp = []
            if column == 6:
                column = 0
                row += 3
            else:
                column += 3
        return True