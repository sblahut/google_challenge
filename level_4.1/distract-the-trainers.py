####    NOTES
####
####    each match - 2 guards
####    guard with fewest bananas will bet all - min
####    other guard will match 
####    winner receives all
####    same number of bananas will not thumb wrestle
####    most bananas + over confidence = loss
####    once both have same number of bananas they will go 
####        back to guarding
####      dont let this happen
####    
####     looking for best combination of thumb wrestling 
####     loop for most time guarding
####
####    number of guards is between 1 > 100
####    number of bananas they start with is between 1 > 1073741823 (i.e. 2^30 -1)
####    matching - edmonds algorithm
####    perfect matching/maximum matching
####
####
class Graph:
    def __init__(self,banana_list):
        self.list_len = len(banana_list)
        self.graph = list([0]*self.list_len for i in xrange(self.list_len))
        for i in xrange(self.list_len):
            for j in xrange(self.list_len):
                if i < j: 
                    self.graph[i][j] = self.dead_lock(banana_list[i], banana_list[j])
                    self.graph[j][i] = self.graph[i][j]  
    
    # identify the greatest common divisor.
    def gcd(self, x, y):
       while(y): x, y = y, x % y
       return x

    # identify where the deadlock or if goes on forever.
    def dead_lock(self, x,y):
        if x == y: return 0
        l = self.gcd(x,y)
        if (x+y) % 2 == 1: return 1
        x,y = x/l,y/l
        x,y = max(x,y), min(x,y)    
        return self.dead_lock(x-y,2*y)

    # identify pairs through bfs.
    def bpm(self, u, matchR, seen):
        for v in range(self.list_len):
            if self.graph[u][v] and seen[v] == False:
                seen[v] = True
                
                # if a has been matched to b, retrieve a from match[b]
                # check if it can be matched to another number given the 
                # current seen list. If so, updated match[b] to c (current)
                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen):
                    matchR[v] = u
                    return True
        return False

    def maxGaurdPair(self):
        matchR = [-1] * self.list_len
        result = 0
        for i in range(self.list_len):
            seen = [False] * self.list_len
            if self.bpm(i, matchR, seen):
                result += 1
        return self.list_len- 2*(result/2)


def solution(l):
    return Graph(l).maxGaurdPair()