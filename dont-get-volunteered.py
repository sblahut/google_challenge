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

import math

def soluution (src, dest):

    def check_paths(x, y):
        pos_paths = [(x+2, y+1), (x+2, y-1),
                    (x-2, y+1), (x-2, y-1),
                    (x+1, y+2), (x+1, y-2),
                    (x-1, y+2), (x-1, y-2)
        ]
        paths = []
        for a, b in pos_paths:
            if 0 <= a < 8 and 0 <= b < 8:
                paths.append[(a, b)]