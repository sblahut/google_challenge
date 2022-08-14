####    NOTES
####
####  
#### raw sample -> end state 
#### state 1 transitions to any state including state 1 
#### solution(m) takes an array nonnegative int that shows how many changes to next state
#### returns array of ints
####    for each terminal state given exact probabilities of terminal state
#### numerator for each state
#### The denominator will fit within a signed 32-bit integer during the calculation, 
#### as long as the fraction is simplified regularly. 
#### 
####    absorbing markov chain
####    > 1 absorbing state
####    possible to go from non-absorbing state to absorbing state in specific
####    number of steps
####    standard form
####    get limiting matrix

import numpy as np

# Returns indexes of active & terminal states.
def detect_states(matrix):
    active, terminal = [], []
    for rowN, row in enumerate(matrix):
        (active if sum(row) else terminal).append(rowN)
    return(active,terminal)

# Convert the elements of array in simplest form.
def simplest_form(B):
    B = B.round().astype(int).A1                   # np.matrix --> np.array (flattened array)
    gcd = np.gcd.reduce(B)
    B = np.append(B, B.sum())                      # append the common denom
    return (B / gcd).astype(int)

# Calculates the absorbing probabilities.
def solution(m):
    active, terminal = detect_states(m)
    if 0 in terminal:                              # special case when s0 is terminal
        return [1] + [0]*len(terminal[1:]) + [1]
    m = np.matrix(m, dtype=float)[active, :]       # list --> np.matrix (active states)
    comm_denom = np.prod(m.sum(1))                 # product of sum of all active rows (used later)
    P = m / m.sum(1)                               # divide by sum of row to convert to probability matrix
    Q, R = P[:, active], P[:, terminal]            # separate Q & R
    I = np.identity(len(Q))
    N = (I - Q) ** (-1)                            # calc fundamental matrix
    B = N[0] * R * comm_denom / np.linalg.det(N)   # get absorbing probabilities and get them close to some integer (inverse of matrix)
    return simplest_form(B)