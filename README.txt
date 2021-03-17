numpy needs to be installed

Run the program in command line.
Multiple files can be given as arguments, separated with space.

python main.py {filename}

The program tries to find the path with 20, 150 and 200 moves.
If path is found, it will create a .txt file with the solution.

The algorithm adds numbers to the maze as steps are taken in a following way:
#########  #########  #########
#^      #  #^1     #  #^12    #
#  ## # #  #1 ## # #  #12## # #
#   # # #  #   # # #  #2  # # #
#########  #########  #########

And iterates through the whole maze until there is no movable space anymore, or if the exit has been found.

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
