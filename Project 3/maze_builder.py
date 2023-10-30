import random

# Globals regarding maze building
entrance = 'S'
exit = 'E'

def generate_maze(size):

    # Notation
    cell = '.'
    wall_notation = '#'
    unvisited = 'u'

    # Step 1. Initialize the maze as all walls
    height = size
    width = size
    maze = []
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(unvisited)
        maze.append(line)

    # Step 2. 
    # Find starting block
    starting_height = int(random.random()*height)
    starting_width = int(random.random()*width)
    # Dont start on edge of maze
    if starting_height == 0:
        starting_height += 1
    if starting_height == height-1:
        starting_height -= 1
    if starting_width == 0:
        starting_width += 1
    if starting_width == width-1:
        starting_width -= 1

    # Blocks around starting cell as walls
    maze[starting_height][starting_width] = cell
    walls = []
    walls.append([starting_height-1, starting_width])
    walls.append([starting_height, starting_width-1])
    walls.append([starting_height, starting_width+1])
    walls.append([starting_height+1, starting_width])

    # Step 3. 
    def surroundingCells(rand_wall):
        s_cells = 0
        if (maze[rand_wall[0]-1][rand_wall[1]] == cell):
            s_cells += 1
        if (maze[rand_wall[0]+1][rand_wall[1]] == cell):
            s_cells += 1
        if (maze[rand_wall[0]][rand_wall[1]-1] == cell):
            s_cells +=1
        if (maze[rand_wall[0]][rand_wall[1]+1] == cell):
            s_cells += 1
        return s_cells
    
    while walls:
        # Pick random wall from the list
        rand_wall = walls[int(random.random()*len(walls))-1]

        # Check if it is a left wall
        if (rand_wall[1] != 0):

            # Check if wall divides one unvisited cell on side to side: Mirror cases
            if maze[rand_wall[0]][rand_wall[1]-1] == unvisited and maze[rand_wall[0]][rand_wall[1]+1] == cell:
                # Find the number of surrounding cells
                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = cell

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != cell):
                            maze[rand_wall[0]-1][rand_wall[1]] = wall_notation
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])
                    # Bottom cell
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != cell):
                            maze[rand_wall[0]+1][rand_wall[1]] = wall_notation
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    # Leftmost cell
                    if (rand_wall[1] != 0):	
                        if (maze[rand_wall[0]][rand_wall[1]-1] != cell):
                            maze[rand_wall[0]][rand_wall[1]-1] = wall_notation
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)
                continue
        
        # Check if it is an upper wall
        if (rand_wall[0] != 0):
            if (maze[rand_wall[0]-1][rand_wall[1]] == unvisited and maze[rand_wall[0]+1][rand_wall[1]] == cell):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = cell

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != cell):
                            maze[rand_wall[0]-1][rand_wall[1]] = wall_notation
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                    # Leftmost cell
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1]-1] != cell):
                            maze[rand_wall[0]][rand_wall[1]-1] = wall_notation
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])

                    # Rightmost cell
                    if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != cell):
                            maze[rand_wall[0]][rand_wall[1]+1] = wall_notation
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue
        
        # Check the bottom wall
        if (rand_wall[0] != height-1):
            if (maze[rand_wall[0]+1][rand_wall[1]] == unvisited and maze[rand_wall[0]-1][rand_wall[1]] == cell):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = cell

                    # Mark the new walls
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != cell):
                            maze[rand_wall[0]+1][rand_wall[1]] = wall_notation
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1]-1] != cell):
                            maze[rand_wall[0]][rand_wall[1]-1] = wall_notation
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])
                    if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != cell):
                            maze[rand_wall[0]][rand_wall[1]+1] = wall_notation
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)


                continue

        # Check the right wall
        if (rand_wall[1] != width-1):
            if (maze[rand_wall[0]][rand_wall[1]+1] == unvisited and maze[rand_wall[0]][rand_wall[1]-1] == cell):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = cell

                    # Mark the new walls
                    if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != cell):
                            maze[rand_wall[0]][rand_wall[1]+1] = wall_notation
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != cell):
                            maze[rand_wall[0]+1][rand_wall[1]] = wall_notation
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    if (rand_wall[0] != 0):	
                        if (maze[rand_wall[0]-1][rand_wall[1]] != cell):
                            maze[rand_wall[0]-1][rand_wall[1]] = wall_notation
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue
        
        # Delete the wall from the list anyway
        for wall in walls:
            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                walls.remove(wall)
    
    # Mark the remaining unvisited cells as walls
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == unvisited):
                maze[i][j] = wall_notation
        
    # Set entrance and exit
    for i in range(0, width):
        if (maze[1][i] == cell):
            maze[0][i] = cell
            break
    
    for i in range(width-1, 0, -1):
        if (maze[height-2][i] == cell):
            maze[height-1][i] = cell
            break

    # Note the entrance and exit
    mark_entrance_and_exit(maze)     
    return maze

def mark_entrance_and_exit(maze):
    for i in range(len(maze[0])):
        if maze[0][i] == '.':
            maze[0][i] = entrance
        if maze[-1][i] == '.':
            maze[-1][i] = exit

# Double the scale of a maze
def double_scale_maze(original_maze):
    original_size = len(original_maze)
    new_size = original_size * 2
    scaled_maze = [['#' for _ in range(new_size)] for _ in range(new_size)]
    
    # print("Scaling the maze now\n\n\n")
    for i in range(original_size):
        # print(f"Row: {i}\n\n\n\n")
        for j in range(original_size):
            # print(f"Column: {j}\n\n")
            cell_value = original_maze[i][j]
            # Scaled coordinates: Original value will be top right of 2x2 generated grid
            x = 2 * i
            y = 2 * j + 1
            # print(f"Cell value:  {cell_value}, Cell position: ({i}, {j}), Scaled position: ({x}, {y})")

            # Check for special case
            # Entrance
            if cell_value == 'S':
                # Entrance case: Entrance will always have passage below: S -> [#S], [#.]
                # print("ENTRANCE")
                # Mark scaled position to be entrance
                scaled_maze[x][y] = 'S'
                # Mark below to be passage
                scaled_maze[x+1][y] = '.'
            if cell_value == 'E':
                # Exit case: Exit is always in bottom row and will have passage above. E -> [#.], [#E]
                # print("EXIT")
                # Mark scaled position to be passage
                scaled_maze[x][y] = '.'
                # Mark bottom to be exit
                scaled_maze[x+1][y] = 'E'
            

            # Check if cell is open passage
            if cell_value == '.':
                # Mark scaled position
                scaled_maze[x][y] = '.'
                
                # Check relevant neighbors to determine passage placements, algorithm is top right biased.

                # Check left for passage: If so place passage to left of scaled position
                if j > 0 and original_maze[i][j-1] == '.':
                    scaled_maze[x][y-1] = '.'
                # Check bottom for passage: If so place passage to bottom of scaled position
                if i < original_size-1 and (original_maze[i+1][j] == '.' or original_maze[i+1][j] == 'E'):
                    scaled_maze[x+1][y] = '.'

    return scaled_maze


def print_maze(maze):
    for row in maze:
        print("".join(row))
#maze = generate_maze(20)
#print_maze(maze)
