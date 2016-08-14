"""
Author: Jordan Brown
Date: 8-13-16

Solves the sherlock and valid string problem.

Link to problem: https://www.hackerrank.com/challenges/sherlock-and-valid-string
"""
def can_be_made_valid_in_one_removal_or_less(str):
    # Map each character in str to number of occurrences.
    occurrences = {}
    for i in range(len(str)):
        if str[i] in occurrences:
            occurrences[str[i]] += 1
        else:
            occurrences[str[i]] = 1;

    # Identify a common count of character occurrences and allow a maximum
    # of one character removal.
    commonCount = 0
    firstRemovalFound = False
    for char, count in occurrences.items():
        if commonCount == 0:
            commonCount = count
        elif commonCount == count:
            continue
        elif commonCount != count and not firstRemovalFound and \
                (count - commonCount == 1 or count == 1):
            firstRemovalFound = True
        elif commonCount != count and not firstRemovalFound and \
                (commonCount - count == 1 or commonCount == 1):
            firstRemovalFound = True
            commonCount = count
        else:
            return False
    return True

s = input()
print("YES" if can_be_made_valid_in_one_removal_or_less(s) else "NO")