##### NOTES #####
#
#   solution(src, dest)
#   src = source square
#       where you start
#   dest = destination square
#       where solution is    
#
#   return int (n)
#       n = smallest number of moves from src to dest while
#       only using chess knight's moves.
#   
#   both src and dest fall betwenn 0 > 63
#
#   ### CHESS KNIGHT MOVES ###
#   (that is, two squares in any direction immediately 
#   followed by one square perpendicular to that direction, 
#   or vice versa, in an "L" shape)
#

import math

def pos_to_coords(pos):
    # Converts chessboard position into coordinates.
    x = int(math.floor(pos/8))
    y = int(pos%8)
    return (x, y)


def coords_to_pos(x, y):
   # Converts coordinates to chessboard position.
    return x + y * 8


def get_possible_moves(x, y):
    # Lists coordinates for next move.

    all_moves = []
    all_moves.append((x+2, y+1))
    all_moves.append((x+2, y-1))
    all_moves.append((x-2, y+1))
    all_moves.append((x-2, y-1))
    all_moves.append((x+1, y+2))
    all_moves.append((x+1, y-2))
    all_moves.append((x-1, y+2))
    all_moves.append((x-1, y-2))

    # Ensure moves are within chessboard limitations.
    valid_moves = []
    for (x, y) in all_moves:
        if(x >= 0 and x < 8 and y >= 0  and y < 8):
            valid_moves.append((x, y))

    return valid_moves


def solution(src, dest):
    # Stop counting at dest square.
    if src == dest:
        return 0

    # Get source and destination square.
    src_x, src_y = pos_to_coords(src)
    dst_x, dst_y = pos_to_coords(dest)
    
    # Create a queue with to check possible moves.
    queue = get_possible_moves(src_x, src_y)
    level_queue = []
    level = 0 

    while True:
        level += 1

        # Checks to see which moves are available at this current level.
        for move in queue:
            # Validate to see if we have arrived at dest.
            if move[0] == dst_x and move[1] == dst_y:
                return level

            # Tests one level at a time by building level_queue over queue after testing all possible moves.
            level_queue.extend(get_possible_moves(move[0], move[1]))

        queue = level_queue
        level_queue = []