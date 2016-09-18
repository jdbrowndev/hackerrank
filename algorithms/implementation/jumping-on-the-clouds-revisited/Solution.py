"""
Author: Jordan Brown
Date: 9-18-16

Solves the jumping on the clouds revisited problem.

Link to problem: https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited
"""

n, k = [int(x) for x in input().split(' ')]
c = [int(x) for x in input().split(' ')]

pos = 0
e = 100
while True:
    pos = (pos + k) % n
    if c[pos] == 1:
        e -= 3
    else:
        e -= 1
    if pos == 0:
        break
        
print(e)
