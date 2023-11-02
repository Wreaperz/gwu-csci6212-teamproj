def maze_to_graph(maze):
    rows, cols = len(maze), len(maze[0])
    graph = {}
    start, end = None, None  # Initialize start and end points

    def idx_to_node(row, col):
        return row * cols + col

    for row in range(rows):
        for col in range(cols):
            if maze[row][col] != '#':  # If it's not a wall
                node = idx_to_node(row, col)
                if node not in graph:
                    graph[node] = []

                if maze[row][col] == 'S':
                    start = node
                elif maze[row][col] == 'E':
                    end = node

                # Check the neighbors (up, down, left, right)
                # Up
                if row - 1 >= 0 and maze[row - 1][col] != '#':
                    graph[node].append(idx_to_node(row - 1, col))
                # Down
                if row + 1 < rows and maze[row + 1][col] != '#':
                    graph[node].append(idx_to_node(row + 1, col))
                # Left
                if col - 1 >= 0 and maze[row][col - 1] != '#':
                    graph[node].append(idx_to_node(row, col - 1))
                # Right
                if col + 1 < cols and maze[row][col + 1] != '#':
                    graph[node].append(idx_to_node(row, col + 1))

    return graph, start, end\

def node_to_idx(node, cols):
    return divmod(node, cols)

def graph_path_to_maze_coordinates(path, cols):
    return [node_to_idx(node, cols) for node in path]

