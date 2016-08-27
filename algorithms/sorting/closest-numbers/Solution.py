"""
Author: Jordan Brown
Date: 8-27-16

Solves the closest numbers problem.

Link to problem: https://www.hackerrank.com/challenges/closest-numbers
"""

# Get array, sort in ascending order.
size = int(input())
arr = [int(x) for x in input().split()]
arr.sort()

# Find and group by difference for all elements at indices i, i - 1.
diffToPairs = {}
for i in range(1, size):
    diff = abs(arr[i] - arr[i - 1])
    if diff in diffToPairs:
        diffToPairs[diff].append((arr[i - 1], arr[i]))
    else:
        diffToPairs[diff] = [(arr[i - 1], arr[i])]

# Find smallest difference, print all elements in the group.
minDiff = min(diffToPairs.keys())
output = ''.join(("{0} {1} ".format(x, y) for x, y in diffToPairs[minDiff])).strip()
print(output)