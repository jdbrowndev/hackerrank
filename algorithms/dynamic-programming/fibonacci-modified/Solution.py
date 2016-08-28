"""
Author: Jordan Brown
Date: 8-27-16

Solves the Fibonacci modified problem via dynamic programming.

Link to problem: https://www.hackerrank.com/challenges/fibonacci-modified
"""

(prev, current, n) = (int(x) for x in input().split())
next = None
for i in range(3, n + 1):
    next = prev + current * current
    prev = current
    current = next
print(next)