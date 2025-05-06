# A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot receives an array of integers commands, which represents a sequence of moves that it needs to execute. There are only three possible types of instructions the robot can receive:

# -2: Turn left 90 degrees.
# -1: Turn right 90 degrees.
# 1 <= k <= 9: Move forward k units, one unit at a time.
# Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, it will stay in its current location (on the block adjacent to the obstacle) and move onto the next command.

# Return the maximum squared Euclidean distance that the robot reaches at any point in its path (i.e. if the distance is 5, return 25).

# Note:

# There can be an obstacle at (0, 0). If this happens, the robot will ignore the obstacle until it has moved off the origin. However, it will be unable to return to (0, 0) due to the obstacle.
# North means +Y direction.
# East means +X direction.
# South means -Y direction.
# West means -X direction.

            di = (di - 1) % 4
    return max_distance

def robotSim(commands: List[int], obstacles: List[List[int]]) -> int:
        elif cmd == -1:
            di = (di + 1) % 4
        else:
            for _ in range(cmd):
                if (x + dx[di], y + dy[di]) not in obstacleSet:
                    x += dx[di]
                    y += dy[di]
                    max_distance = max(max_distance, x*x + y*y)
                else:
                    break

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = y = di = 0
    obstacleSet = set(map(tuple, obstacles))
    max_distance = 0

        if cmd == -2:
    for cmd in commands: