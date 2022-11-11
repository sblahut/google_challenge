####    NOTES
####
####    2D Grid, flat
####    Current cell is determined by 4 nearby cells
####
####    (1) that cell,
####    (2) the cell below it,
####    (3) the cell to the right of it,
####    (4) the cell below and to the right of it.
####
####    If cell(1)-(4) in 2x2 block (neighborhood)
####          gas in next state
####    elsif 
####          the cell will be empty in the next state.
####
####    Sounds like Conway's game of life (react sample project)
####
####    Note: 1 fewer row and column due to bottom and rightmost cells not having 
####       them, respectively.
####
import itertools

def solution(g):
    g = tuple(zip(*g))
    
    previous_row = {}
    for row in row_generator(len(g[0])):
        previous_row[row] = 1

    for i in range(len(g)):
        current_row = {}
        for row in row_generator(len(g[0])):
            for combination, count in previous_row.iteritems():
                if is_valid(row, combination, g[i]):
                    # new gas state.
                    if row in current_row:
                        current_row[row] += count
                    # state stays the same.
                    else:
                        current_row[row] = count
        previous_row = current_row

    return sum(previous_row.values())

# define whether gas is in cell or not.
STATES = (0, 1)

# build layout.
def row_generator(row_len):
    return itertools.product(STATES, repeat=row_len+1)

# check for gas in 2x2 grid.
def is_valid(r1, r2, row_check):
    for i in range(len(row_check)):
        sum_cells = r1[i] + r1[i+1] + r2[i] + r2[i+1]
        if (sum_cells == 1) != row_check[i]:
            return False
    return True