from maze_builder import *
from maze_to_graph import *
import time

# Main function: Uses Depth-First search to find the appropriate path
def dfs(maze, start, target):
    stack = [(start, [])]
    visited = set()

    # Define possible directions: up, down, left, right
    directions = [(-1, 0, 'D'), (1, 0, 'U'), (0, -1, 'R'), (0, 1, 'L')]

    while stack:
        current, path = stack.pop()
        x, y = current

        if current == target:
            return path

        visited.add(current)

        for dx, dy, symbol in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and \
                    maze[nx][ny] in ['.', 'E'] and (nx, ny) not in visited:
                stack.append(((nx, ny), path + [(nx, ny, symbol)]))

    return []

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

    start_time = time.time()
    path = dfs(maze, start, target)
    end = time.time() - start_time
    print("time taken: " + str(end) + " seconds")

    if path:
        print("There is a path")
        mark_path(maze, path)
        return True
    print("There is no path")
    return False

# print("Found Route:", result)
# Print the new maze (with lines pointing back from end to start)
# print_maze(maze)

# Generate a maze of X by X proportions
n = 15
maze = generate_maze(n)
# print_maze(maze)

# doubled_maze = double_scale_maze(maze)
# print("\nPrinting scaled maze\n")
# print_maze(doubled_maze)

# # Convert the maze into a graph
# # graph = maze_to_graph(maze)
# # print(graph)

# Print out whether or not a route was found
# print("\nPrinting result\n\n")
result = find_target(maze)
traversed_maze = maze
# print_maze(traversed_maze)

# Singularize the path in the maze
singularized_maze = singularize_maze(traversed_maze)
print(f"\nPrinting maze with singular path")
print_maze(singularized_maze)

# Try the branching algorithm
add_branches_to_maze(singularized_maze, 4)
print(f"\nPrinting maze with branch")
print_maze(singularized_maze)
