"""
Author: Jordan Brown
Date: 9-3-16

Finds the minimum number of operations required to convert strings into palindromes.

Link to problem: https://www.hackerrank.com/challenges/the-love-letter-mystery
"""
def get_minimum_operations_to_palindrome(s):
    cost = 0
    for i in range(int(len(s)/2)):
        if s[i] != s[len(s) - 1 - i]:
            cost += abs(ord(s[i]) - ord(s[len(s) - 1 - i]))
    return cost

t = int(input())
for _ in range(t):
    print(get_minimum_operations_to_palindrome(input()))