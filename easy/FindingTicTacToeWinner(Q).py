# Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

# Players take turns placing characters into empty squares ' '.
# The first player A always places 'X' characters, while the second player B always places 'O' characters.
# 'X' and 'O' characters are always placed into empty squares, never on filled ones.
# The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

# You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        return board[0][0]
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0]:
            return board[i][0]
    
    return "Draw" if len(moves) == 9 else "Pending"

def tictactoe(moves: List[List[int]]) -> str:
    board = [[None]*3 for _ in range(3)]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]:
        return board[0][2]
    
    for i, (row, col) in enumerate(moves):
        player = 'A' if i % 2 == 0 else 'B'
        board[row][col] = player
    
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i]:
            return board[0][i]