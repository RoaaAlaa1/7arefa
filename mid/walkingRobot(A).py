def robotSim(commands: List[int], obstacles: List[List[int]]) -> int:
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = y = di = 0
    obstacleSet = set(map(tuple, obstacles))
    max_distance = 0

    for cmd in commands:
        if cmd == -2:  # Turn left
            di = (di - 1) % 4
        elif cmd == -1:  # Turn right
            di = (di + 1) % 4
        else:  # Move forward
            for _ in range(cmd):
                if (x + dx[di], y + dy[di]) not in obstacleSet:
                    x += dx[di]
                    y += dy[di]
                    max_distance = max(max_distance, x*x + y*y)
                else:
                    break
    return max_distance