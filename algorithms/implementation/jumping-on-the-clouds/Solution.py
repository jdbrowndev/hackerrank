"""
Author: Jordan Brown
Date: 9-18-16

Uses a greedy algorithm to solve the jumping on the clouds problem.

Link to problem: https://www.hackerrank.com/challenges/jumping-on-the-clouds
"""

n = int(input())
c = [int(x) for x in input().split(' ')]
pos = 0
steps = 0
while pos < len(c) - 1:
    # If we're one step away from the finish or we can't take two steps,
    # take only one step.
    if pos == len(c) - 2 or c[pos + 2] == 1:
        pos += 1
    # Else, take two steps.
    else:
        pos += 2
    steps += 1
print(steps)