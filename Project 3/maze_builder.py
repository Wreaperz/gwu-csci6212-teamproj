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

# Function used to mark the correct path
def mark_path(maze, path):
    for x, y, symbol in path:
        if maze[x][y] == '.':
            maze[x][y] = symbol

def singularize_maze(maze):
    """
    Takes a maze that has been traversed by dfs with path marked, then makes that the only path.
    """
    path_symbols = {'U', 'D', 'L', 'R'}
    special_chars = {'S', 'E'}
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] in path_symbols:
                maze[i][j] = '.'
            elif maze[i][j] in special_chars:
                continue
            else:
                maze[i][j] = '#'
    return maze

def add_branches_to_maze(maze, num_branches):
    # Store all paths into a set
    path_locations = []  # Stores coordinates of locations in the maze where there is a path
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == '.':
                path_locations.append([i, j])
    path_locations = set(path_locations)
    
    max_branch_size = len(maze)
    min_branch_size = len(maze / 4)

    directions = {"left": (-1, 0), "right": (1, 0), "down": (0, -1), "up": (0, 1)}
    opposite_directions = {"left": "right", "right": "left", "up": "down", "down": "up"}

    for branch in range(num_branches):

        # Pick a random starting location
        starting_y, starting_x = random.choice(path_locations)

        # Remove all adjacent locations to starting position: Split into x and y to prevent confusion
        starting_adjacent_left_x, starting_adjacent_left_y = starting_x - 1, starting_y
        starting_adjacent_right_x, starting_adjacent_right_y = starting_x + 1, starting_y
        starting_adjacent_above_x, starting_adjacent_above_y = starting_x, starting_y + 1
        starting_adjacent_below_x, starting_adjacent_below_y = starting_x, starting_y - 1

        starting_adjacent_left = [starting_adjacent_left_y, starting_adjacent_left_x]
        starting_adjacent_right = [starting_adjacent_right_y, starting_adjacent_right_x]
        starting_adjacent_above = [starting_adjacent_above_y, starting_adjacent_above_x]
        starting_adjacent_below = [starting_adjacent_below_y, starting_adjacent_below_x]

        starting_adjacents = [starting_adjacent_left, starting_adjacent_right, starting_adjacent_above, starting_adjacent_below]

        ### ------------------------------------- ### Continue debugging here

        for starting_adjacent in starting_adjacents:
            if starting_adjacent in path_locations:
                path_locations.remove(starting_adjacent)

        # Pick a random branch length
        path_length = random.randint(min_branch_size, max_branch_size)
        current_length = 0

        # Directions record
        previous_direction = None
        current_direction = None

        # Define current location and adjacents
        current_x = None
        current_y = None
        current_adjacent_left_x, current_adjacent_left_y = None, None
        current_adjacent_right_x, current_adjacent_right_y = None, None
        current_adjacent_above_x, current_adjacent_above_y = None, None
        current_adjacent_below_x, current_adjacent_below_y = None, None
        
        # Travel through the entire path
        stop = False
        while current_length < path_length or not stop:
            # List of direction possibilities
            direction_possibilities = ["left", "right", "up", "down"]

            # If just starting
            if current_direction is None:
                # Pick a direction based on starting_adjacents to current location
                # If adjacents are on exterior of maze
                # Adjacent left
                if starting_adjacent_left[0] == 0 or starting_adjacent_left[1] == 0 or starting_adjacent_left[1] == len(maze) - 1:
                    direction_possibilities.remove("left")
                # Adjacent right
                if starting_adjacent_right[0] == len(maze) - 1 or starting_adjacent_right[1] == 0 or starting_adjacent_right[1] == len(maze) - 1:
                    direction_possibilities.remove("right")
                # Adjacent above
                if starting_adjacent_above[0] == 0 or starting_adjacent_above[0] == len(maze) - 1 or starting_adjacent_above[1] == 0:
                    direction_possibilities.remove("up")
                # Adjacent below
                if starting_adjacent_below[0] == 0 or starting_adjacent_below[0] == len(maze) - 1 or starting_adjacent_below[1] == len(maze) - 1:
                    direction_possibilities.remove("down")
                
                # Dont travel into previous path
                # Left
                if maze[starting_adjacent_left[0]][starting_adjacent_left[1]] == '.':
                    if "left" in direction_possibilities:
                        direction_possibilities.remove("left")
                # Right
                if maze[starting_adjacent_right[0]][starting_adjacent_right[1]] == '.':
                    if "right" in direction_possibilities:
                        direction_possibilities.remove("right")
                # Above
                if maze[starting_adjacent_above[0]][starting_adjacent_above[1]] == '.' or maze[starting_adjacent_above[0]][starting_adjacent_above[1]] == 'S':
                    if "up" in direction_possibilities:
                        direction_possibilities.remove("up")
                # Below
                if maze[starting_adjacent_below[0]][starting_adjacent_below[1]] == '.' or maze[starting_adjacent_below[0]][starting_adjacent_below[1]] == 'E':
                    if "down" in direction_possibilities:
                        direction_possibilities.remove("down")
                
                # Check to make sure there are still possible directions
                if len(direction_possibilities) == 0:
                    print("NO POSSIBLE DIRECTIONS TO TRAVEL: NEED TO INVESTIGATE AND HANDLE THIS CASE")
                    print(f"Location is: ({starting_y}, {starting_x})")
                    exit(1)
                
                # Randomly pick a remaining direction to travel
                current_direction = random.choice(direction_possibilities)
                dx, dy = directions[current_direction]

                # Travel to new location
                current_x = starting_x + dx
                current_y = starting_y + dy

                # Define new adjacents
                current_adjacent_left = [current_y, current_x - 1]
                current_adjacent_right = [current_y, current_x + 1]
                current_adjacent_above = [current_y + 1, current_x]
                current_adjacent_below = [current_y - 1, current_x]

                # Increment path length
                current_length += 1
                
            # If continuing along path
            else:
                # Consider previous direction if applicable
                if previous_direction is not None:
                    if previous_direction != current_direction:
                        direction_possibilities.remove(previous_direction)
                
                # Dont travel opposite to current direction
                direction_possibilities.remove(opposite_directions[current_direction])

                # Pick a direction based on starting_adjacents to current location
                # If adjacents are on exterior of maze
                # Adjacent left
                if current_adjacent_left[0] == 0 or current_adjacent_left[1] == 0 or current_adjacent_left[1] == len(maze) - 1:
                    if "left" in direction_possibilities:
                        direction_possibilities.remove("left")
                # Adjacent right
                if current_adjacent_right[0] == len(maze) - 1 or current_adjacent_right[1] == 0 or current_adjacent_right[1] == len(maze) - 1:
                    if "right" in direction_possibilities:
                        direction_possibilities.remove("right")
                # Adjacent above
                if current_adjacent_above[0] == 0 or current_adjacent_above[0] == len(maze) - 1 or current_adjacent_above[1] == 0:
                    if "up" in direction_possibilities:
                        direction_possibilities.remove("up")
                # Adjacent below
                if current_adjacent_below[0] == 0 or current_adjacent_below[0] == len(maze) - 1 or current_adjacent_below[1] == len(maze) - 1:
                    if "down" in direction_possibilities:
                        direction_possibilities.remove("down")
                
                # Dont travel into previous path
                # Left
                if maze[current_adjacent_left[0]][current_adjacent_left[1]] == '.':
                    if "left" in direction_possibilities:
                        direction_possibilities.remove("left")
                # Right
                if maze[current_adjacent_right[0]][current_adjacent_right[1]] == '.':
                    if "right" in direction_possibilities:
                        direction_possibilities.remove("right")
                # Above
                if maze[current_adjacent_above[0]][current_adjacent_above[1]] == '.' or maze[current_adjacent_above[0]][current_adjacent_above[1]] == 'S':
                    if "up" in direction_possibilities:
                        direction_possibilities.remove("up")
                # Below
                if maze[current_adjacent_below[0]][current_adjacent_below[1]] == '.' or maze[current_adjacent_below[0]][current_adjacent_below[1]] == 'E':
                    if "down" in direction_possibilities:
                        direction_possibilities.remove("down")

                # Check to make sure there are still possible directions if not end path short
                if len(direction_possibilities) == 0:
                    print("NO POSSIBLE DIRECTIONS TO TRAVEL: ENDING PATH SHORT")
                    print(f"Location is: ({starting_y}, {starting_x})")
                    stop = True

                # Slight Bias traveling in the current direction to avoid excessive zagging
                if current_direction in direction_possibilities:
                    for i in range(2):
                        direction_possibilities.append(current_direction)

                # Randomly pick a remaining direction to travel
                previous_direction = current_direction
                current_direction = random.choice(direction_possibilities)
                dx, dy = directions[current_direction]

                # Travel to new location
                current_x = starting_x + dx
                current_y = starting_y + dy

                # Define new adjacents
                current_adjacent_left = [current_y, current_x - 1]
                current_adjacent_right = [current_y, current_x + 1]
                current_adjacent_above = [current_y + 1, current_x]
                current_adjacent_below = [current_y - 1, current_x]

                # Increment path length
                current_length += 1








                
                


            
                        







    



def print_maze(maze):
    for row in maze:
        print("".join(row))
#maze = generate_maze(20)
#print_maze(maze)
