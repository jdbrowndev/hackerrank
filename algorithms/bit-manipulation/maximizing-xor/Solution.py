"""
Author: Jordan Brown
Date: 10-21-16

Solves the maximizing XOR problem.

Link to problem: https://www.hackerrank.com/challenges/maximizing-xor
"""

l, r, maxXor = (int(input()), int(input()), 0)
for a in range(l, r + 1):
    for b in range(a, r + 1):
        xor = a^b
        if xor > maxXor:
            maxXor = xor
print(maxXor)