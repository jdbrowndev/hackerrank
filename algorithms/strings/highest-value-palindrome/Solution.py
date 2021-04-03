"""
Author: Jordan Brown
Date: 4-3-21

Solves the highest value palindrome problem.

Link to problem: https://www.hackerrank.com/challenges/richie-rich/problem
"""

def highestValuePalindrome(s, n, k):
    result = list(s)
    offset = 0
    mismatches = 0
    for _ in range(n//2):
        c1 = s[offset]
        c2 = s[n - 1 - offset]

        if c1 != c2:
            mismatches += 1

        offset += 1

    if mismatches > k:
        return "-1"

    offset = 0
    for _ in range(n//2):
        c1 = s[offset]
        c2 = s[n - 1 - offset]

        if k > 1 and k > mismatches and (c1 != "9" and c2 != "9"):
            result[offset] = "9"
            result[n - 1 - offset] = "9"
            k -= 2
        elif c1 != c2:
            greater = c1 if int(c1) > int(c2) else c2
            result[offset] = greater
            result[n - 1 - offset] = greater
            k -= 1

        if c1 != c2:
            mismatches -= 1
        offset += 1

    if k > 0 and n % 2 == 1:
        result[n//2] = "9"
    
    return "".join(result)