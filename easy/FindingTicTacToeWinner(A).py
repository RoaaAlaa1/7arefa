def tictactoe(moves: List[List[int]]) -> str:
    # Initialize the board
    board = [[None]*3 for _ in range(3)]
    
    # Fill the board with moves
    for i, (row, col) in enumerate(moves):
        player = 'A' if i % 2 == 0 else 'B'
        board[row][col] = player
    
    # Check all possible winning conditions
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0]:
            return board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i]:
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]:
        return board[0][2]
    
    # Check if game is pending or draw
    return "Draw" if len(moves) == 9 else "Pending"