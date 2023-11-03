from maze_to_graph import maze_to_graph, graph_path_to_maze_coordinates
from maze_builder import add_branches_to_maze, build_maze_with_branches, print_maze, build_singular_maze
from main import graph_dfs

import time
import matplotlib.pyplot as plt


def record_graphing_data(maze_size, num_data_points, min_branch_size, max_branch_size):
    """
    Returns a list of measured times it takes dfs to traverse a number of generated graphs.
    """

    # Create the singular maze
    singularized_maze = build_singular_maze(maze_size)

    # Define parameters
    branch_nums = [2 * i for i in range(num_data_points)]

    # Generate the graphs
    graph_data = create_graph_data(singularized_maze, branch_nums, min_branch_size, max_branch_size)

    # Record the sizes of each graph
    graph_sizes = [len(graph_data[i][0]) for i in range(len(graph_data))]

    # Sort the graphs by sizes
    # Combine the sizes with the graph data for sorting
    combined = list(zip(graph_sizes, graph_data))

    # Sort based on the sizes just in case path number isnt 1 to 1 with graph size
    sorted_combined = sorted(combined, key=lambda x: x[0])
    # Unzip them back into sorted graph sizes and sorted graph data
    sorted_graph_sizes, sorted_graph_data = zip(*sorted_combined)
    # Convert them back to lists if needed
    sorted_graph_sizes = list(sorted_graph_sizes)
    sorted_graph_data = list(sorted_graph_data)

    measured_times = []

    # Measure the time it takes dfs to traverse each graph
    for i in range(len(graph_data)):
        graph = graph_data[i][0]
        start = graph_data[i][1]
        end = graph_data[i][2]

        start_time = time.perf_counter_ns()
        path = graph_dfs(graph, start, end)
        end_time = time.perf_counter_ns()
        elapsed_time = end_time - start_time
        measured_times.append(elapsed_time)

    return graph_sizes, measured_times

def create_graph_data(singularized_maze, branch_num_list, min_branch_size, max_branch_size):
    """
    Creates mazes with specified numbers of branches and returns a list of graphs
    """
    graphs = []
    # print("Printing singularized maze before: \n")
    # print_maze(singularized_maze)
    for i in range(len(branch_num_list)):
        maze_with_branches = add_branches_to_maze(singularized_maze, branch_num_list[i], min_branch_size, max_branch_size)
        graph, start, end = maze_to_graph(maze_with_branches)
        graph_tuple = (graph, start, end)
        graphs.append(graph_tuple)
    
    # print("\nPrinting singularized maze after: \n")
    # print_maze(singularized_maze)

    return graphs


def plot_graph_size_vs_time(sizes, times):
    plt.figure(figsize=(10, 6))  # Set the figure size as desired
    plt.plot(sizes, times, marker='o', label='Experimental Times')  # Plot measured times

    # Calculate theoretical times assuming linear time complexity
    min_size = min(sizes)
    max_size = max(sizes)
    min_time = min(times)
    max_time = max(times)

    a = (max_time - min_time) / (max_size - min_size)
    b = min_time - a * min_size

    theoretical_times = [a * size + b for size in sizes]

    plt.plot(sizes, theoretical_times, label='Theoretical Times')  # Plot theoretical times
    plt.title('Graph Size vs Time Taken for DFS')  # Title of the plot
    plt.xlabel('Graph Size')  # Label for the x-axis
    plt.ylabel('Time Taken (nanoseconds)')  # Label for the y-axis
    plt.grid(True)  # Add grid for better readability
    plt.legend()  # Add a legend
    plt.show()  # Display the plot

maze_size = 200
num_data_points = 100
min_branch_size = 5
max_branch_size = 5

sizes, times = record_graphing_data(maze_size, num_data_points, min_branch_size, max_branch_size)

plot_graph_size_vs_time(sizes, times)


