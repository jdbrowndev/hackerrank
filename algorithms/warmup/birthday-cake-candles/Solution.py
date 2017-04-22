"""
Author: Jordan Brown
Date: 4-21-17

Solves the birthday cake candles problem.

Link to problem: https://www.hackerrank.com/challenges/birthday-cake-candles
"""
def get_number_of_candles_blown(candles):
    occurrences = {}
    tallest = 0
    for c in candles:
        tallest = c if c > tallest else tallest;
        if c in occurrences:
            occurrences[c] += 1
        else:
            occurrences[c] = 1
    return occurrences[tallest]
    

n = int(input())
candles = [int(x) for x in input().split(' ')]
print(get_number_of_candles_blown(candles))