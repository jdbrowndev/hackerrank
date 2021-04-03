"""
Author: Jordan Brown
Date: 4-3-21

Solves the array manipulation problem.

Link to problem: https://www.hackerrank.com/challenges/crush/problem
"""

def arrayManipulation(n, queries):
    array = [0] * n
    for query in queries:
        [a, b, k] = query
        array[a - 1] += k
        if b < n:
            array[b] -= k

    current = 0
    max = 0
    for i in range(n):
        current += array[i]
        max = current if current > max else max

    return max