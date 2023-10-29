import random

def generate_maze(size):
    # Initialize maze with walls everywhere
    maze = [['#' for _ in range(size)] for _ in range(size)]
    
    stack = []
    moves = [(0, 2), (2, 0), (0, -2), (-2, 0)]  # right, down, left, up

    def is_valid_move(x, y):
        return 0 <= x < size and 0 <= y < size  # Adjusted to include the outer boundary

    def get_unvisited_neighbors(x, y):
        neighbors = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny) and maze[nx][ny] == '#':
                neighbors.append((nx, ny))
        return neighbors

    start_x, start_y = 0, random.randint(1, size // 4) * 2  # Now it's in the wall at the top-left
    end_x, end_y = 2 * random.randint(3 * size // 8, size // 2 - 1) + 1, size - 1

    maze[start_x][start_y] = 'S'  # Marking start
    maze[end_x][end_y] = 'E'  # Marking end

    stack.append((start_x, start_y))

    while stack:
        x, y = stack[-1]
        neighbors = get_unvisited_neighbors(x, y)

        if neighbors:
            nx, ny = random.choice(neighbors)

            # Carve a passage
            maze[(x + nx) // 2][(y + ny) // 2] = '.'
            maze[nx][ny] = '.'

            stack.append((nx, ny))
        else:
            stack.pop()

    return maze

def print_maze(maze):
    for row in maze:
        print("".join(row))

#maze = generate_maze(20)
#print_maze(maze)
