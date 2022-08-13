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
#   time complexity for BFS on a graph is O(V + E) O(V+E); where V is the number of vertices and E is the number of edges.

def solution (src, dest):
    
    # define all possible knight moves.
    def check_paths(x, y):
        pos_paths = [(x+2, y+1), (x+2, y-1),
                    (x-2, y+1), (x-2, y-1),
                    (x+1, y+2), (x+1, y-2),
                    (x-1, y+2), (x-1, y-2)
        ]
        # ensure moves are within chessboard limitations.
        paths = []
        for a, b in pos_paths:
            if 0 <= a < 8 and 0 <= b < 8:
                paths.append((a, b))

        return paths

    def bfs(s, d):
        
        # stop counting at destination square.
        if s == d:
            return 0

        from collections import deque
        x = s[0]
        y = s[1]
        q = deque([(x, y, 0)])
        visited = {(x, y): 1}

        while q:
            u, v, count = q.popleft()
            paths = check_paths(u, v)
            for path in paths:
                if path == d:
                    return count+1
                if path not in visited:
                    visited[path] = 1
                    q.append((path[0], path[1], count+1))
        return -1

    def convert_coord(x):   
        # row.
        r = int(x//8)
        # column.
        c = int(x%8)
        return(r, c)

    s = convert_coord(src)
    d = convert_coord(dest)
    return bfs(s, d)