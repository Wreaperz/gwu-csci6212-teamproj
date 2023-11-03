import random
import copy

def define_adjacents(coordinate_x, coordinate_y):
    """
    Defines and returns a dictionary of immediate adjacents to the current position.
    """
    adjacent_left_x, adjacent_left_y = coordinate_x - 1, coordinate_y
    adjacent_right_x, adjacent_right_y = coordinate_x + 1, coordinate_y
    adjacent_above_x, adjacent_above_y = coordinate_x, coordinate_y - 1
    adjacent_below_x, adjacent_below_y = coordinate_x, coordinate_y + 1

    adjacent_left = (adjacent_left_y, adjacent_left_x)
    adjacent_right = (adjacent_right_y, adjacent_right_x)
    adjacent_above = (adjacent_above_y, adjacent_above_x)
    adjacent_below = (adjacent_below_y, adjacent_below_x)

    adjacents_dict = {"left": adjacent_left, "right": adjacent_right, "above": adjacent_above, "below": adjacent_below}
    return adjacents_dict

def define_corners(coordinate_x, coordinate_y):
    """
    Defines and returns a dictionary of points on the corners to the current position.
    """

    top_left_x, top_left_y = coordinate_x - 1, coordinate_y - 1
    top_right_x, top_right_y = coordinate_x + 1, coordinate_y - 1
    bottom_left_x, bottom_left_y = coordinate_x - 1, coordinate_y + 1
    bottom_right_x, bottom_right_y = coordinate_x + 1, coordinate_y + 1

    top_left = (top_left_y, top_left_x)
    top_right = (top_right_y, top_right_x)
    bottom_left = (bottom_left_y, bottom_left_x)
    bottom_right = (bottom_right_y, bottom_right_x)

    corners_dict = {"top_left": top_left, "top_right": top_right, "bottom_left": bottom_left, "bottom_right": bottom_right}
    return corners_dict

    
def remove_adjacents(adjacents_dict, path_locations):
    """
    Removes all adjacent paths to coordinate in path_locations. Returns a list of removed coordinates for debugging.
    """

    removed_coords = []

    for adjacent_coord in adjacents_dict.values():
        if adjacent_coord in path_locations:
            path_locations.remove(adjacent_coord)
    
    return removed_coords

def eliminate_directions_regarding_two_aways(maze, direction_possibilities, current_x, current_y):
    """
    Eliminates directions leading to tiles adjacent to existing paths by analyzing positions two tiles away from the current position.
    Calculations can be avoided if the tile is not defined.
    """
    # Add check for 2 away
    # Left
    if current_x > 1:
        two_away_left = maze[current_y][current_x - 2]
        if two_away_left == '.':
            if "left" in direction_possibilities:
                direction_possibilities.remove("left")
    # Right
    if current_x < len(maze) - 2:
        two_away_right = maze[current_y][current_x + 2]
        if two_away_right == '.':
            if "right" in direction_possibilities:
                direction_possibilities.remove("right")
    # Down
    if current_y < len(maze) - 2:
        two_away_down = maze[current_y + 2][current_x]
        if two_away_down == '.' or two_away_down == 'E':
            if "down" in direction_possibilities:
                direction_possibilities.remove("down")
    # Up
    if current_y > 1:
        two_away_up = maze[current_y - 2][current_x]
        if two_away_up == '.' or two_away_up == 'S':
            if "up" in direction_possibilities:
                direction_possibilities.remove("up")


def eliminate_directions_regarding_corners(maze, direction_possibilities, corners):
    """
    Similar functionality to eliminate_directions_regarding_adjacents. Modifies direction_possibilities in place to remove directions
    regarding constraints with points diagonal to the current position. Prevents overlapping paths.
    """

    # Extract corner points from dictionary in cartesian form for simplicity
    top_left_x, top_left_y = corners["top_left"][1], corners["top_left"][0]
    top_right_x, top_right_y = corners["top_right"][1], corners["top_right"][0]
    bottom_left_x, bottom_left_y = corners["bottom_left"][1], corners["bottom_left"][0]
    bottom_right_x, bottom_right_y = corners["bottom_right"][1], corners["bottom_right"][0]

    # Define corner points in maze
    top_left = maze[top_left_y][top_left_x]
    top_right = maze[top_right_y][top_right_x]
    bottom_left = maze[bottom_left_y][bottom_left_x]
    bottom_right = maze[bottom_right_y][bottom_right_x]

    # Top left
    if top_left == '.' or top_left == 'S':
        # Remove up and left
        if "up" in direction_possibilities:
            direction_possibilities.remove("up")
        if "left" in direction_possibilities:
            direction_possibilities.remove("left")
    # Top right
    if top_right == '.' or top_right == 'S':
        # Remove up and right
        if "up" in direction_possibilities:
            direction_possibilities.remove("up")
        if "right" in direction_possibilities:
            direction_possibilities.remove("right")
    # Bottom left
    if bottom_left == '.' or bottom_left == 'E':
        # Remove down and left
        if "down" in direction_possibilities:
            direction_possibilities.remove("down")
        if "left" in direction_possibilities:
            direction_possibilities.remove("left")
    # Bottom right
    if bottom_right == '.' or bottom_right == 'E':
        # Remove down and right
        if "down" in direction_possibilities:
            direction_possibilities.remove("down")
        if "right" in direction_possibilities:
            direction_possibilities.remove("right")


def consider_previous_direction(direction_possibilities, current_direction, previous_direction):
    """
    Removes direction that lead to side by side pathing with previous paths. Returns True or False depending on if action was taken based on previous direction.
    Modifies direction_possibilities in place.
    """
    if previous_direction:
        if previous_direction != current_direction:
            direction_possibilities.remove(previous_direction)
            return True
        
    return False


def remove_backtracking(direction_possibilities, current_direction):
    """
    Removes the opposite direction to the current direction from direction_possibilities if current_direction is not None. 
    Returns true if current_direction is not None, false otherwise.
    """
    if current_direction:
        opposites = {"left": "right", "right": "left", "up": "down", "down": "up"}
        opposite_direction = opposites[current_direction]
        if opposite_direction in direction_possibilities:
            direction_possibilities.remove(opposite_direction)
        
        return True
    
    return False


def eliminate_directions_regarding_adjacents(maze, direction_possibilities, adjacents):
    """
    Eliminates directions regarding constraints that can be handled with adjacent points. Modifies the maze and direction_possibilities in place.
    """
    # Avoid the exterior of the maze
    avoid_maze_exterior(direction_possibilities, adjacents, len(maze))

    # Avoid running into previous paths
    # print(f"Maze is now: {print_maze(maze)}\n\n\n\n")
    avoid_adjacent_paths(maze, direction_possibilities, adjacents)

  
def avoid_adjacent_paths(maze, direction_possibilities, adjacents):
    """
    Eliminates directions that lead into previous adjacent paths. Modifies the direction_possibilities in place.
    """

    # Extract adjacent points from dictionary in cartesian form for simplicity
    adjacent_left_x, adjacent_left_y = adjacents["left"][1], adjacents["left"][0]
    adjacent_right_x, adjacent_right_y = adjacents["right"][1], adjacents["right"][0]
    adjacent_above_x, adjacent_above_y = adjacents["above"][1], adjacents["above"][0]
    adjacent_below_x, adjacent_below_y = adjacents["below"][1], adjacents["below"][0]

    # Dont travel into previous path
    # Left
    # print(f"Adjacents are: {adjacents}")
    if within_maze_bounds(len(maze), adjacent_left_x, adjacent_left_y):
        if maze[adjacent_left_y][adjacent_left_x] == '.':
            if "left" in direction_possibilities:
                direction_possibilities.remove("left")
    # Right
    if within_maze_bounds(len(maze), adjacent_right_x, adjacent_right_y):
        if maze[adjacent_right_y][adjacent_right_x] == '.':
            if "right" in direction_possibilities:
                direction_possibilities.remove("right")
    # Above
    if within_maze_bounds(len(maze), adjacent_above_x, adjacent_above_y):
        if maze[adjacent_above_y][adjacent_above_x] == '.' or maze[adjacent_above_y][adjacent_above_x] == 'S':
            if "up" in direction_possibilities:
                direction_possibilities.remove("up")
    # Below
    if within_maze_bounds(len(maze), adjacent_below_x, adjacent_below_y):
        if maze[adjacent_below_y][adjacent_below_x] == '.' or maze[adjacent_below_y][adjacent_below_x] == 'E':
            if "down" in direction_possibilities:
                direction_possibilities.remove("down")


def avoid_maze_exterior(direction_possibilities, adjacents, maze_size):
    """
    Eliminates directions that lead into the exterior wall of the maze. Modifies the direction_possibilities list in place.
    """

    # Extract adjacent points from dictionary in cartesian form for simplicity
    adjacent_left_x, adjacent_left_y = adjacents["left"][1], adjacents["left"][0]
    adjacent_right_x, adjacent_right_y = adjacents["right"][1], adjacents["right"][0]
    adjacent_above_x, adjacent_above_y = adjacents["above"][1], adjacents["above"][0]
    adjacent_below_x, adjacent_below_y = adjacents["below"][1], adjacents["below"][0]

    # Left
    if not within_maze_exterior(maze_size, adjacent_left_x, adjacent_left_y):
        # print("Left adjacent is not within maze exterior\n")
        if "left" in direction_possibilities:
            direction_possibilities.remove("left")
    # Right
    if not within_maze_exterior(maze_size, adjacent_right_x, adjacent_right_y):
        # print("Right adjacent is not within maze exterior\n")
        if "right" in direction_possibilities:
            direction_possibilities.remove("right")
    # Above
    if not within_maze_exterior(maze_size, adjacent_above_x, adjacent_above_y):
        # print("Above adjacent is not within maze exterior\n")
        if "up" in direction_possibilities:
            direction_possibilities.remove("up")
    # Below
    if not within_maze_exterior(maze_size, adjacent_below_x, adjacent_below_y):
        # print("Below adjacent is not within maze exterior\n")
        if "down" in direction_possibilities:
            direction_possibilities.remove("down")

def within_maze_exterior(maze_size, coordinate_x, coordinate_y):
    """
    Returns True if point is contained within the exterior of the maze. 
    Returns False if the point is on the edge of the maze.
    """
    return 0 < coordinate_x < maze_size - 1 and 0 < coordinate_y < maze_size - 1

def within_maze_bounds(maze_size, coordinate_x, coordinate_y):
    """
    Returns True if point is contained within the bounds of the maze. False otherwise.
    """
    return 0 <= coordinate_x <= maze_size - 1 and 0 <= coordinate_y <= maze_size - 1

def pick_direction(maze, current_x, current_y, current_direction, previous_direction, adjacents, corners):
    """
    Picks a new direction for the path based on surrounding points, previous directions, and maze exterior bounds.
    params:

    - maze_size: Size of the square maze. (int)
    - current_x: x coordinate of current position. (int)
    - current_y: y coordinate of current position. (int)
    - current_direction: (string) or None
    - previous direction: (string) or None
    - adjacents: adjacent coordinate dictionary returned by define_adjacents function. (dictionary)
    - corners: corners coordinate dictionary returned by define_corners function. (dictionary)
    - two_aways: Coordinates of points two tiles away in cardinal directions. Returned by define_two_aways function. (dictionary)

    Returns: A tuple containing the new current direction and previous direction. (Tuple)
    """
    # List of direction possibilities
    direction_possibilities = ["left", "right", "up", "down"]

    # Remove the opposite direction to the current direction to avoid backtracking. Returns false if at the beginning of new branch.
    at_beginning = remove_backtracking(direction_possibilities, current_direction)

    # Consider the previous direction if not starting new branch
    if not at_beginning:
        consider_previous_direction(direction_possibilities, current_direction, previous_direction)

    # Eliminate directions regarding adjacents
    eliminate_directions_regarding_adjacents(maze, direction_possibilities, adjacents)

    # Eliminate directions regarding corners
    # Possible for all direction possibilities to be removed at this point. Avoid unnecessary calculations if so.
    if direction_possibilities:
        eliminate_directions_regarding_corners(maze, direction_possibilities, corners)

    # Eliminate directions regarding points two tiles away: Prevents tunneling into tiles adjacent to existing paths.
    # Points two tiles away are calculated dynamically within function as they are not always defined.
    if direction_possibilities:
        eliminate_directions_regarding_two_aways(maze, direction_possibilities, current_x, current_y)

    # If there is no way to go, return None for current direction. The path must be cut short.
    if not direction_possibilities:
        return (None, previous_direction)
    
    # print(f"Current direction options are now: {direction_possibilities}\n")

    # Bias the current direction to prevent excessive zagging.
    if current_direction in direction_possibilities:
        for i in range(2):
            direction_possibilities.append(current_direction)
    
    # Modify the previous direction
    previous_direction = current_direction
    
    # Pick a random direction
    current_direction = random.choice(direction_possibilities)

    # print(f"Current direction is now: {current_direction}\n")

    # Modify the previous direction
    return (current_direction, previous_direction)

def add_branches_to_maze(maze, num_branches, min_branch_size, max_branch_size):
    """
    Adds a specified number of branches with randomly generated lengths between defined bounds. Returns a maze with branches at the end.
    """
    maze_with_branches = copy.deepcopy(maze)

    # Store all paths into a set 
    path_locations = [] # Stores coordinates of locations in the maze where there is a path
    for i in range(len(maze_with_branches)):
        for j in range(len(maze_with_branches[0])):
            if maze_with_branches[i][j] == '.':
                path_locations.append((i, j))
    path_locations = set(path_locations)

    # Directions dictionary to store actions
    directions = {"left": (-1, 0), "right": (1, 0), "down": (0, 1), "up": (0, -1)}

    for branch in range(num_branches):

        # Pick a random starting location
        current_y, current_x = random.choice(list(path_locations))

        # Find all adjacent points to starting position
        adjacents = define_adjacents(current_x, current_y)

        # Remove all adjacent points to starting position
        removed_adjacents = remove_adjacents(adjacents, path_locations)
        # print(f"Removed adjacents to: ({current_y}, {current_x}) are: {removed_adjacents}")

        # Pick a random branch length
        path_length = random.randint(min_branch_size, max_branch_size)
        
        # Define current length
        current_length = 0

        # Directions memory
        previous_direction = None
        current_direction = None

        # Max iterations for safety
        iterations = 0
        max_iterations = 5 * max_branch_size

        # Create the path
        while current_length < path_length and iterations < max_iterations:

            iterations += 1

            # Calculate adjacents: Redundant on first iteration
            if iterations > 1:
                adjacents = define_adjacents(current_x, current_y)

            # Calculate corner points
            corners = define_corners(current_x, current_y)

            # Pick direction
            current_direction, previous_direction = pick_direction(maze_with_branches, current_x, current_y, current_direction, previous_direction, adjacents, corners)

            # Exit path early if no where to go
            if current_direction is None:
                # print(f"No where to go. Ending branch {branch} early. Path length is: {current_length}.")
                break

            # Create path in current direction and update position
            dx, dy = directions[current_direction]
            current_x += dx
            current_y += dy
            maze_with_branches[current_y][current_x] = '.'

            # Increment path length
            current_length += 1
    
    return maze_with_branches