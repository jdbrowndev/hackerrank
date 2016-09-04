"""
Author: Jordan Brown
Date: 9-3-16

Finds the minimum number of operations required to transform a string into an anagram
of another string.

Link to problem: https://www.hackerrank.com/challenges/anagram
"""
def get_number_of_operations_to_anagram(s1, s2):
    
    # s1 cannot be made an anagram of s2 if their lengths are different.
    if len(s1) != len(s2):
        return -1
    
    # Map each character in s1 to number of occurrences.
    occurrences = {}
    for char in s1:
        if char in occurrences:
            occurrences[char] += 1
        else:
            occurrences[char] = 1
    
    # Subtract common characters in s2 from occurrences.
    for char in s2:
        if char in occurrences:
            occurrences[char] -= 1
            if occurrences[char] == 0:
                occurrences.pop(char, None)
    
    # Cost = sum of uncommon characters between s1 and s2.
    return sum(occurrences.values())
    

t = int(input())
for _ in range(t):
    tcase = input()
    s1, s2 = tcase[:int(len(tcase)/2)], tcase[int(len(tcase)/2):]
    print(get_number_of_operations_to_anagram(s1, s2))