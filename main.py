from maze_builder import *
from maze_to_graph import *

# Generate a maze of X by X proportions
maze = generate_maze(30)
print_maze(maze)

print("\n")

# Convert the maze into a graph
graph = maze_to_graph(maze)
print(graph)


# Main function: Uses Depth-First search to find the appropriate path
def dfs(maze, current, target, visited, path):
    x, y = current
    if current == target:
        return True

    # Define possible directions: up, down, left, right
    directions = [(-1, 0, '↓'), (1, 0, '↑'), (0, -1, '→'), (0, 1, '←')]

    for dx, dy, symbol in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and \
            maze[nx][ny] in ['.', 'E'] and (nx, ny) not in visited:
            visited.add((nx, ny))
            if dfs(maze, (nx, ny), target, visited, path):
                path.append((nx, ny, symbol))
                return True

    return False

# Function used to mark the correct path
def mark_path(maze, path):
    for x, y, symbol in path:
        if maze[x][y] == '.':
            maze[x][y] = symbol

# Function used to find whether or not a path out exists
def find_target(maze):
    start = None
    target = None

    # Find start and target positions
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            if maze[i][j] == 'E':
                target = (i, j)

    if not start or not target:
        return False

    path = []
    found = dfs(maze, start, target, set(), path)
    if found:
        mark_path(maze, path)
        return True
    return False

# Print out whether or not a route was found
print("Found Route:", find_target(maze))

# Print the new maze (with lines pointing back from end to start)
print_maze(maze)
