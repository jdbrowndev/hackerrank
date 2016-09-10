"""
Author: Jordan Brown
Date: 9-9-16

Uses a greedy algorithm to solve the cutting boards problem.

Link to problem: https://www.hackerrank.com/challenges/board-cutting
"""

# The algorithm for this problem is simple. Perform cuts in order from largest
# cost to smallest cost. Keep track of the number of vertical/horizontal cuts made
# as the total cost is computed.
def get_minimum_cutting_cost(verticalCuts, horizontalCuts):
    verticalCuts.sort(reverse = True)
    horizontalCuts.sort(reverse = True)
    
    verticalCostMultiplier = 1
    horizontalCostMultiplier = 1
    totalCost = 0
    
    for _ in range(len(verticalCuts) + len(horizontalCuts)):
        if len(horizontalCuts) == 0 or (len(verticalCuts) > 0 and verticalCuts[0] > horizontalCuts[0]):
            # Do a vertical cut.
            totalCost += horizontalCostMultiplier*verticalCuts.pop(0)
            verticalCostMultiplier += 1
        else:
            # Do a horizontal cut.
            totalCost += verticalCostMultiplier*horizontalCuts.pop(0)
            horizontalCostMultiplier += 1
    
    # Not sure why the problem requires that the total cost be mod by 10^9 + 7, but it's
    # needed for a correct answer.
    return totalCost % (10**9 + 7)

# Compute each test case.
t = int(input())
for _ in range(t):
    m, n = [int(x) for x in input().split()]
    verticalCuts = [int(x) for x in input().split()]
    horizontalCuts = [int(x) for x in input().split()]
    print(get_minimum_cutting_cost(verticalCuts, horizontalCuts))