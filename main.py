import numpy as np
import sys


def main():

    if len(sys.argv) < 2:
        print("Maze files needed. Give them separated with a space")
        sys.exit()
    else:
        files = []
        maxmoves = [20, 150, 200]
        for i in range(1, len(sys.argv)):
            files.append(str(sys.argv[i]))
    for file in files:
        maze, original_maze, location = load_file_to_array(file)
        exit_location = None
        for maxmove in maxmoves:
            current_maze = np.copy(maze)
            file_parameters = (file, maxmove)
            # search_paths() creates a new maze that contains paths with given moves, if there is a person lost in maze
            if location is not None:
                maze_paths, moves, exit_location = search_paths(current_maze, location, maxmove)
            # Creates an text file of the maze, if solved
            if exit_location is not None:
                create_solution(maze_paths, original_maze, moves, exit_location, file_parameters)
                break


def create_solution(maze, original_maze, moves, location, file_parameters):
    """Creates an array containing correct moves and a text file for visualization

    Parameters
    ----------
    maze : array(int)
        Array that contains the new maze with all paths
    original_maze : array(string)
        Array that contains the original maze
    moves: int
        Moves used for finding solution
    location : list(int)
        Location of the found exit in array
    file_parameters : tuple(string, int)
        Contains information for creating a new file: name and moves used
    """

    path = []
    # Loop for finding the correct path from exit to the first location entered
    while moves != 1:
        neighbours = find_neighbours(maze, location)
        for neighbour in neighbours:
            if neighbour is not None:
                # If the neighbour is one integer less, adds the location to path array
                # and takes the location to variable location, that will be explored in the next iteration
                if neighbour[2] == moves - 1:
                    path.append([neighbour[0], neighbour[1]])
                    location = [neighbour[0], neighbour[1]]
                    moves -= 1
                    break

    # Creates a new maze array with the original layout and adds the path with 'o' chars
    newmaze = np.copy(original_maze)
    for point in path:
        newmaze[point[0]][point[1]] = 'o'

    # Creates a text file from the array
    solvedfile = file_parameters[0].split(".")
    newfilename = "{}_in_{}_moves.txt".format(solvedfile[0], str(file_parameters[1]))
    solve_file = open(newfilename, "w")
    for line in newmaze:
        for item in line:
            solve_file.write(str(item))


def search_paths(maze, location, max_moves):
    """Algorithm for finding the paths to exit

    Parameters
    ----------
    maze: array(int)
        Array that contains the maze to be solved
    location: list(int)
        Contains the location of starting point
    max_moves: int
        The amount of moves that the algorithm is allowed to make

    Returns
    -------
    maze: array(int)
        Array of the maze with the paths made with algorithm
    i: int
        Moves made
    exit_location: list(int)
        Contains the exit location if found, otherwise it is None
    """

    # Moves made in maze
    i = 0

    # Locations to be explored, initialized with starting point
    locations = [location]

    # Loop for exploring the maze
    while True:
        nosolution = True
        newlocations = []
        for location in locations:
            # Finds each neighbour of the current location
            neighbours = find_neighbours(maze, location)
            for neighbour in neighbours:
                if neighbour is not None:
                    # If the neighbour is movable space
                    if neighbour[2] == 0:
                        nosolution = False
                        # Sets the neighbour to one value higher than current location
                        # And appends the neighbour to a list that will be explored on next iteration
                        maze[neighbour[0]][neighbour[1]] = i + 1
                        newlocations.append([neighbour[0], neighbour[1]])
                    # If the neighbour is exit
                    elif neighbour[2] == -2:
                        # Sets the exit to one value higher than current location
                        # And sets the exit to a newlocations list, but this time the next iteration won't be executed
                        maze[neighbour[0]][neighbour[1]] = i + 1
                        newlocations.append([neighbour[0], neighbour[1]])
                        print("Solution found with {} moves!".format(max_moves))
                        return maze, i + 1, newlocations[len(newlocations) - 1]
        i += 1

        # If all locations have been explored and they have no neighbours with movable space
        if nosolution:
            print("There is no solution for this maze")
            break

        # If maximum moves allowed has been reached
        elif i == max_moves:
            print("There is no solution for this maze with {} moves.".format(max_moves))
            break

        for item in newlocations:
            locations.append(item)

    return maze, i, None


def find_neighbours(maze, location):
    """Finds and returns the neighbours of a location in the maze

    Parameters
    ----------
    maze: array(int)
        Array of the maze
    location: list(int)
        Current location

    Returns
    -------
    neighbours: list(int)
        List that contains location of north, east, south and west neighbours and their items
    """
    if location[1] - 1 >= 0:
        north = (location[0], location[1] - 1, maze[location[0]][location[1] - 1])
    else:
        north = None

    if location[0] + 1 < len(maze):
        east = (location[0] + 1, location[1], maze[location[0] + 1][location[1]])
    else:
        east = None

    if location[1] + 1 < len(maze[location[0]]):
        south = (location[0], location[1] + 1, maze[location[0]][location[1] + 1])
    else:
        south = None

    if location[0] - 1 >= 0:
        west = (location[0] - 1, location[1], maze[location[0] - 1][location[1]])
    else:
        west = None
    neighbours = [north, east, south, west]
    return neighbours


def load_file_to_array(file):
    """Opens the maze file and creates an array containing the maze

    Parameters
    ----------
    file: string
        Name of the file

    Returns
    -------
    maze: array(int)
        Array of the maze, where strings have been converted to integers
    original_maze: array(string)
        Array containing the maze without any changes
    location: list(int)
        Starting location in the array
    """

    # Tries if the file exists in directory
    try:
        mazefile = open(file, "r")
    except FileNotFoundError:
        print("{} not found. Closing program.".format(file))
        sys.exit()

    # Checks if file is .txt
    filetest = file.split(".")
    if filetest[1] != 'txt':
        print("Closing program. File needs to be .txt".format(file))
        sys.exit()

    # Counts the length of the maze for initializing arrays
    y_count = 0
    x_count = 0
    for lines in mazefile:
        y_count += 1
        if y_count == 1:
            x_count = len(lines)

    maze = np.zeros((y_count, x_count), dtype=int)
    original_maze = np.zeros((y_count, x_count), dtype=str)
    mazefile = open(file, "r")
    location = None
    x, y = 0, 0
    try:
        for lines in mazefile:
            for char in lines:
                original_maze[y][x] = char
                if char == '#':
                    maze[y][x] = -1
                elif char == '^':
                    maze[y][x] = 1
                    # Saves the starting location
                    location = [y, x]
                elif char == 'E':
                    maze[y][x] = -2
                else:
                    # If file contains strings that are not allowed, program will be closed
                    if char != '\n' and char != ' ':
                        print("File is in bad format. Closing program.")
                        sys.exit()
                x += 1
            y += 1
            x = 0
    except IndexError:
        print("Maze needs to be rectangle. Closing program.")
        sys.exit()
    return maze, original_maze, location


if __name__ == "__main__":
    main()
