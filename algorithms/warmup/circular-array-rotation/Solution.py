"""
Author: Jordan Brown
Date: 8-16-16

Solves the circular array rotation problem via modular arithmetic.

Link to problem: https://www.hackerrank.com/challenges/circular-array-rotation
"""
n, k, q = (int(x) for x in input().split())
arr = input().split()
for _ in range(q):
    m = int(input())
    
    # Explanation:
    # k % n normalizes the number of rotations to [0..n-1]
    # n - k % n returns the index where arr now begins
    # ((n - k % n) + m) % n adds the query index and normalizes it to [0..n-1]
    print(arr[((n - k % n) + m) % n])