####    NOTES
####
####    beams loss damage over distance
####    beam hits corner = same direction
####    beam hits me/bunny trainer = stops immediately
####    room dimensions between 1 >=1250
####    x = me y = trainer or vice versa
####    
####    ___________________________
####    solution(dimensions, your_position, trainer_position, distance)
####    roomDimensions = [1 < x_dim <= 1250, 1 < y_dim <= 1250]
####    maxDistanceToCauseDamage = 1 < distance <= 10000
#### 
#### 
####       width/height of room = [var x, var y]  
####       x and y coords of me in room = [var x, var y]
####       x and y coords of trainer in room = [var x, var y]
####
####            if distinctDirectionsToHitTrainer > maxDistanceToCauseDamage
####                 distinctDirectionsToHitTrainer = -1     
####            return distinctDirectionsToHitTrainer
####
####            if myLocation && trainerLocation == slope   ## beams hits me
####                 beamHitsMe = -1
####            return beamHitsMe
####
from itertools import product
from math import atan2

def solution(dimensions, your_position, trainer_position, distance):
    x0, y0 = your_position
    hits = dict()
    for position in your_position, trainer_position:
        for reflect in product(*[range(-(distance // -d) + 1) for d in dimensions]):
            for quadrant in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
                x, y = [
                    (d * r + (d - p if r % 2 else p)) * q
                    for d, p, r, q in zip(dimensions, position, reflect, quadrant)
                ]
                # calc distance using Pythagorean theorem.
                travel = (abs(x - x0) ** 2 + abs(y - y0) ** 2) ** 0.5
                bearing = atan2(x0 - x, y0 - y)
                if travel > distance or bearing in hits and travel > abs(hits[bearing]):
                    continue
                # mark self-hits with a negative value.
                hits[bearing] = travel * (-1 if position == your_position else 1)
    return len([1 for travel in hits.values() if travel > 0])

