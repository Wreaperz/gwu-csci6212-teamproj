from maze_builder import *
from maze_to_graph import maze_to_graph, node_to_idx, graph_path_to_maze_coordinates
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


def graph_dfs(graph, start, target):
    # The stack holds tuples of the current node and the path taken to reach it
    stack = [(start, [])]  
    # A set to keep track of visited nodes
    visited = set()  

    while stack:
        current, path = stack.pop()  
       
        # If the target is found, return the path
        if current == target:  
            return path
        
        # Mark the current node as visited
        visited.add(current)  

        # Iterate over the neighbors
        for neighbor in graph[current]:  
            if neighbor not in visited:
                # For each neighbor, create a new tuple with the neighbor and the path including this move
                stack.append((neighbor, path + [neighbor]))

    # If the target is not reachable, return an empty list
    return []  

# Generate a maze of X by X proportions
maze_size = 20
num_branches = 5
min_branch_size = 2
max_branch_size = 10
maze_with_branches = build_maze_with_branches(maze_size, num_branches, min_branch_size, max_branch_size)

# Print the graph of the maze
graph, start, end = maze_to_graph(maze_with_branches)
print(f"Graph is: \n\n\n")
print(f"{graph}")
print(f"\n\nStart is: {start}, End is: {end}")
path = graph_dfs(graph, start, end)
print(f"\n\nPath in graph nodes is: {path}\n\n")
path_in_coordinates = graph_path_to_maze_coordinates(path, len(maze_with_branches))
print(f"\nPath in maze coordinates is: {path_in_coordinates}\n\n")
print(f"Maze is: \n")
print_maze(maze_with_branches)

