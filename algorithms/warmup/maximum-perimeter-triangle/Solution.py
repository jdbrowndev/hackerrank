"""
Author: Jordan Brown
Date: 10-8-16

Solves the maximum perimeter triangle problem.

Link to problem: https://www.hackerrank.com/challenges/maximum-perimeter-triangle
"""
def get_maximum_perimeter_triangle(sticks):
    sticks.sort()
    i = len(sticks) - 1
    while i - 2 >= 0:
        if sticks[i - 2] + sticks[i - 1] > sticks[i]:
            return (sticks[i - 2], sticks[i - 1], sticks[i])
        i -= 1
    return (-1,)

n = int(input())
sticks = [int(x) for x in input().split()]
print(" ".join([str(i) for i in get_maximum_perimeter_triangle(sticks)]))