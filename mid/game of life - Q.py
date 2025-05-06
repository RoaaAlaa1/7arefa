# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

# Given the current state of the board, update the board to reflect its next state.

# Note that you do not need to return anything.


            for di, dj in directions:
    
    # Update the board with new values
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == -1:
                board[i][j] = 0
            elif board[i][j] == 2:
                board[i][j] = 1

def gameOfLife(board: List[List[int]]) -> None:
                if 0 <= ni < rows and 0 <= nj < cols and abs(board[ni][nj]) == 1:
                    live_neighbors += 1

    if not board:
        return
    
    rows = len(board)
    cols = len(board[0])
    
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),          (0,1),
                  (1,-1),  (1,0), (1,1)]

        for i in range(rows):
        for j in range(cols):
            live_neighbors = 0
                ni, nj = i + di, j + dj

            # Apply rules
            if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[i][j] = -1
            elif board[i][j] == 0 and live_neighbors == 3:
                board[i][j] = 2