"""
Author: Jordan Brown
Date: 9-3-16

Solves the funny string problem.

Link to problem: https://www.hackerrank.com/challenges/funny-string
"""
def is_funny_string(s):
    for i in range(1, len(s)):
        originalDiff = abs(ord(s[i]) - ord(s[i - 1]))
        reverseDiff = abs(ord(s[len(s) - i - 1]) - ord(s[len(s) - i]))
        if originalDiff != reverseDiff:
            return False
    return True

t = int(input())
for _ in range(t):
    print("Funny" if is_funny_string(input()) else "Not Funny")