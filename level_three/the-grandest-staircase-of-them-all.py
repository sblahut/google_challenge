####    NOTES
####
####    
####    *restrictions
####    staricase = more than 2 steps
####    no two steps will be = height
####    each step should be lower height than previous step
####    each step must have one brick
####    step height = total n of bricks that make up current step
####    example: N = 3
####    step 1 - height = 2     #
####    step 2 - height = 1     ##
####                            21
####        when n = 4
####        #
####        #
####        ##
####        31
####        when n = 5 there are two possilble staircase solutions
####
####    solution(n) make sure integer is positive and 
####        return # of staircases
####    from n bricks
####    n > 3 < 200 to save $$$$
####    top down - time complexity of O(n)
####    tabular method - bottom up approach seems favorable.

def solution(n):
    # memory
    m = [[0 for i in range(n + 1)] for j in range(n + 1)]
    m[0][0] = 1  # base case equals 1 staricase.
    
    
    for stair in range(1, n + 1):
        # stair height.
        
	    for left in range(0, n + 1):
	        # bricks left.
	        
	        # staircases made with stair height and bricks left.
            # equals staricases we can make with last stair height -1 and bricks left remaining
                # this ensures a smaller step proceeding forward.
            # compare against [m].
	        m[stair][left] = m[stair - 1][left]
            if left >= stair:
	            # create a new step with smaller height and extra bricks.
	            m[stair][left] += m[stair - 1][left - stair]
	
	# remove invalid case due to base case assumption.          	
    return m[n][n] -1