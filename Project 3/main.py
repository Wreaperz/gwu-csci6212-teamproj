from maze_builder import *
from maze_to_graph import *
from maze_builder import build_maze_with_branches
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

# Generate a maze of X by X proportions
maze_size = 200
num_branches = 100
min_branch_size = 2
max_branch_size = 10
maze_with_branches = build_maze_with_branches(maze_size, num_branches, min_branch_size, max_branch_size)
