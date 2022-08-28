####    NOTES
####
####  Code changes daily
####  Commander gets list daily, see which lists contains codes
####  "lucky triples"
####  (x, y, z) = x divides y and y divides z i.e. (1, 2, 4)
####  which lists matches locks on door
####    i.e. a list with 5 passcodes = list with 5 "lucky triples"
####  solution(l) l = list of positive integers
####    counts number of "lucky triples" of (Li, Lj, Lk) 
####        list indices meet i < j < k
####
#### The length of l is between 2 and 2000 inclusive.  
#### The elements of l are between 1 and 999999 inclusive.
#### 32-bit signed integer.
#### return o on zero "lucky triples"
####
#### % operator appears to be too expensive at O(n^3)
####    more reaserch on something lower

def solution(ar):
    c = [0] * len(l)
    count = 0
    for i in range(0,len(l)):
        for j in range(0, i):
            if l[i] % l[j] == 0:
                c[i] = c[i] + 1
                count = count + c[j]
    return count

ar = [1, 2, 3, 4, 5, 6]
print(solution(ar))

