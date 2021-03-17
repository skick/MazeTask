numpy needs to be installed

Run the program in command line.
Multiple files can be given as arguments, separated with space.

python main.py {filename}

The program tries to find the path with 20, 150 and 200 moves.
If path is found, it will create a .txt file with the solution.

The algorithm iterates through a list of locations and finds the location's neighbours. If the neighbour is a movable space, it will add a one value greater number to it
and add the neighbour to the list of locations.

The iteration starts with value 0 and only one position: the starting position.
Here is an example:

#########  #########  #########  ######### 
#^      #  #^1     #  #^12    #  #^123   #
#  ## # #  #1 ## # #  #12## # #  #12## # #
#   # # #  #   # # #  #2  # # #  #23 # # #
#########  #########  #########  #########

The program iterates through the whole maze until there is no movable space anymore, or if the exit has been found.

If exit is found, it will create a path by going from the exit to the starting position, by always going to a neighbour tile
with a smaller number in each iteration.

Example of a maze:

######################################
#       # ###      ##    ###  #      #
# ### # #     ### #### #  ##  # ###  #
#   # # # ##### #       #  ## # # #  #
# ### #   ##    #######  # #  # # #  #
#   # # # #  ## #      # # #    # #  #
# ### # # # #   # #### # # # ## # #  #
#   # # # # # ###    # # # #         #
# # # # ### # # #### # # #   #########
#   # #   # # #   ^  # # # # #       #
# # # ## ## # ## ##### # # #   ##### #
#   #     # #    #   # # # #####     #
# #########  ##### # ##  #       #####
#         ##       #    ## ####### # E
######### ################ #       # #
#         #            #     ####### #
# ######### ###### # # # #####       #
#   #   #   #      # # ### # # #######
# #   #   # # #### # #               #
######################################

'#' = Wall
' ' = Movable space
'E' = Exit
'^' = Person lost
