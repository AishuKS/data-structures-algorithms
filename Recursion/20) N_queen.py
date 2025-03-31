'''
The n-queens is the problem of placing n queens on n × n chessboard such that no two queens can attack each other. Given an integer n, return all distinct solutions to the n -queens puzzle. Each solution contains a distinct boards configuration of the queen's placement, where ‘Q’ and ‘.’ indicate queen and empty space respectively.

Input: n = 4

Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

Explanation: There exist two distinct solutions to the 4-queens puzzle as shown below

'''
def swap(row, col, board, n):
    duprow = row
    dupcol = col
    while row>=0 and col>=0:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1
    
    row = duprow
    col = dupcol
    while col>=0:
        if board[row][col] == 'Q':
            return False
        col-=1
    
    row = duprow
    col = dupcol
    while row<n and col>=0:
        if board[row][col] == 'Q':
            return False
        row+=1
        col-=1
    
    return True

def solve(col, ans, n, board):
    if col == n:
        ans.append(list(board))
        return
    for row in range(n):
        if swap(row, col, board, n):
            board[row] = board[row][:col] + 'Q' + board[row][col+1:]    
            solve(col+1, ans, n, board)
            board[row] = board[row][:col] + '.' + board[row][col+1:]
            
ans = []
n = 4
board = ['.'*n for i in range(n)]
solve(0, ans, n, board)
print(ans)