"""
Author: Jordan Brown
Date: 9-19-16

Solves the ice cream parlor problem.

Link to problem: https://www.hackerrank.com/challenges/icecream-parlor
"""

def get_2_flavors_for_m_dollars(flavors, m):
    
    # First, create a dict for O(1) lookup.
    
    # This problem is complicated by the fact that flavors can have
    # duplicate costs. Each cost must map to a list of indices where
    # that cost occurs.
    
    flavorsToIds = {}
    index = 1
    for f in flavors:
        if f in flavorsToIds:
            flavorsToIds[f].append(index)
        else:
            flavorsToIds[f] = [index]
        index += 1
    
    for f in flavors:
    
        # Before searching for a flavor to pair with f, delete f so f isn't paired
        # with itself by accident.
        i = flavorsToIds[f][0]
        del flavorsToIds[f][0]
        if len(flavorsToIds[f]) == 0:
            del flavorsToIds[f]
            
        if m - f in flavorsToIds:
            return (i, flavorsToIds[m - f][0])
            
    return None

t = int(input())
for _ in range(t):
    m = int(input())
    n = int(input())
    flavors = [int(x) for x in input().split()]
    print("{} {}".format(*get_2_flavors_for_m_dollars(flavors, m)))