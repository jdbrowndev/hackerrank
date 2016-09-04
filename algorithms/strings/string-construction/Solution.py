"""
Author: Jordan Brown
Date: 9-3-16

Solves the string construction problem.

Link to problem: https://www.hackerrank.com/challenges/string-construction
"""
def get_minimum_construction_cost(s):
    cost = 0
    p = ""
    for char in s:
        if char not in p:
            p += char
            cost += 1
    return cost

n = int(input())
for _ in range(n):
    print(get_minimum_construction_cost(input()))