def maze_to_graph(maze):
    rows, cols = len(maze), len(maze[0])
    graph = {}

    # Convert a 2D maze index to a unique node key
    def idx_to_node(row, col):
        return row * cols + col

    for row in range(rows):
        for col in range(cols):
            if maze[row][col] == '.':  # This is an open space and hence a node
                node = idx_to_node(row, col)
                if node not in graph:
                    graph[node] = []

                # Check the neighbors
                # Up
                if row - 1 >= 0 and maze[row - 1][col] == '.':
                    graph[node].append(idx_to_node(row - 1, col))
                # Down
                if row + 1 < rows and maze[row + 1][col] == '.':
                    graph[node].append(idx_to_node(row + 1, col))
                # Left
                if col - 1 >= 0 and maze[row][col - 1] == '.':
                    graph[node].append(idx_to_node(row, col - 1))
                # Right
                if col + 1 < cols and maze[row][col + 1] == '.':
                    graph[node].append(idx_to_node(row, col + 1))

    return graph

# Example
maze = [
    ['#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '#'],
    ['#', '.', '#', '.', '#'],
    ['#', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#']
]

#graph = maze_to_graph(maze)
#print(graph)
