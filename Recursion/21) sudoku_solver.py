def solver(row, col, c, board):
    for i in range(9):
        if board[i][col] == c:
            return False
        if board[row][i] == c:
            return False
        if board[3*(row//3) + (i//3)][3*(col//3) + (i%3)] == c:
            return False
    return True

def sudoku(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                for c in '123456789':
                    if  solver(i,j,c, board):
                        board[i][j] = c
                        if sudoku(board):
                            return True
                        else:
                            board[i][j] = '.'
                return False
    return True
                        
        
        
        
board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]


sudoku(board)
print(board)