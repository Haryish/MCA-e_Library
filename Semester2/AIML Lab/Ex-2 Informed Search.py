import heapq

# Define the maze as an 8x8 matrix
maze = [
    ['S', ' ', ' ', 'X', ' ', 'X', ' ', ' '],
    ['X', 'X', ' ', ' ', ' ', 'X', 'X', ' '],
    [' ', 'X', 'X', 'X', ' ', 'X', ' ', 'X'],
    ['X', ' ', 'X', ' ', ' ', ' ', 'X', ' '],
    ['X', ' ', ' ', 'X', ' ', 'X', ' ', ' '],
    ['X', 'X', ' ', 'X', 'G', 'X', ' ', ' '],
    ['X', ' ', ' ', 'X', ' ', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X', ' ', ' ', ' ', 'X']
]

def printmaze(matrix):
    for row in matrix:
        print()
        for col in row:
            print(col,end=" ")

# Define possible movements (up, down, left, right)
movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def heuristic(node, goal):
    # Manhattan distance heuristic
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def astar_search(maze, start, goal):
    open_set = []
    closed_set = set()

    heapq.heappush(open_set, (0, start, []))  # Priority queue: (f-value, current node, path)

    while open_set:
        _, current, path = heapq.heappop(open_set)

        if current == goal:
            return path + [current]

        if current in closed_set:
            continue

        closed_set.add(current)

        for dx, dy in movements:
            x, y = current
            neighbor = (x + dx, y + dy)

            if (
                0 <= neighbor[0] < len(maze) and
                0 <= neighbor[1] < len(maze[0]) and
                maze[neighbor[0]][neighbor[1]] != 'X'
            ):
                g = len(path) + 1
                h = heuristic(neighbor, goal)
                f = g + h
                heapq.heappush(open_set, (f, neighbor, path + [current]))

    return None  # No path found

start = (0, 0)
goal = (5, 4)
print("Input Map:")
print(printmaze(maze))
print("------------------")
print("Path:")
path = astar_search(maze, start, goal)

if path:
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if (row, col) == start:
                print('S', end=' ')
            elif (row, col) == goal:
                print('G', end=' ')
            elif (row, col) in path:
                print('P', end=' ')  # Path
            else:
                print(maze[row][col], end=' ')
        print()
else:
    print("No path found!")
