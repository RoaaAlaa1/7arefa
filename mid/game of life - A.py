def gameOfLife(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    if not board:
        return
    
    rows = len(board)
    cols = len(board[0])
    
    # Directions for 8 neighbors
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),          (0,1),
                  (1,-1),  (1,0), (1,1)]
    
    for i in range(rows):
        for j in range(cols):
            live_neighbors = 0
            # Count live neighbors
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and abs(board[ni][nj]) == 1:
                    live_neighbors += 1
            
            # Apply rules
            # Rule 1 or 3: cell dies (mark with -1)
            if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[i][j] = -1
            # Rule 4: cell becomes alive (mark with 2)
            elif board[i][j] == 0 and live_neighbors == 3:
                board[i][j] = 2
    
    # Update the board with new values
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == -1:
                board[i][j] = 0
            elif board[i][j] == 2:
                board[i][j] = 1