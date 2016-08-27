"""
Author: Jordan Brown
Date: 8-26-16

Solves the palindrome index problem.

Link to problem: https://www.hackerrank.com/challenges/palindrome-index
"""
def get_palindrome_index(s):
    for i in range(int(len(s)/2)):
        endIndex = len(s) - i - 1
        if s[i] != s[endIndex]:
            if is_palindrome(s[i + 1:endIndex + 1]):
                return i
            elif is_palindrome(s[i:endIndex]):
                return endIndex
            else:
                return -1
    return -1
    
def is_palindrome(s):
    for i in range(int(len(s)/2)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

for _ in range(int(input())):
    print(get_palindrome_index(input()))