"""
Author: Jordan Brown
Date: 10-21-16

Solves the counter game problem.

Link to problem: https://www.hackerrank.com/challenges/counter-game
"""

def is_power_of_2(i):
    return i & (i - 1) == 0

def get_largest_power_of_2_less_than(i):
    largest = 1
    while i > 1:
        i = i >> 1
        largest *= 2
    return largest
        
for _ in range(int(input())):
    turn = 0
    n = int(input())
    while n > 1:
        if is_power_of_2(n):
            n -= int(n/2)
        else:
            n -= get_largest_power_of_2_less_than(n)
        turn += 1
    print("Richard" if turn % 2 == 0 else "Louise")