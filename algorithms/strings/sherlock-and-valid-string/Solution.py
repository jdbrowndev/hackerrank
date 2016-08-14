"""
Author: Jordan Brown
Date: 8-14-16

Solves the sherlock and valid string problem.

Link to problem: https://www.hackerrank.com/challenges/sherlock-and-valid-string
"""
def can_be_made_valid_in_one_removal_or_less(str):

    # First, map each character in str to number of occurrences.
    occurrences = {}
    for i in range(len(str)):
        if str[i] in occurrences:
            occurrences[str[i]] += 1
        else:
            occurrences[str[i]] = 1;
            
    # Second, map each occurrence value to frequency that it appears.
    frequencies = {}
    for v in occurrences.values():
        if v in frequencies:
            frequencies[v] += 1
        else:
            frequencies[v] = 1
    
    # If 3 or more distinct occurrence values exist, one removal won't work.
    if len(frequencies) > 2:
        return False
    
    # If all characters occur the same number of times, no removal is needed.
    if len(frequencies) == 1:
        return True
    
    # At this point, len(frequencies) must equal 2.
    
    # If there's a single stray character, we can remove that character.
    if 1 in frequencies and frequencies[1] == 1:
        return True
    
    # If an occurrence value is 1 greater than the other, and that occurrence
    # value only happens once, we can decrement that occurrence value.
    keys = list(frequencies.keys())
    lesser = keys[0] if keys[0] < keys[1] else keys[1]
    greater = keys[1] if keys[0] < keys[1] else keys[0]
    if greater - lesser == 1 and frequencies[greater] == 1:
        return True
    
    # Else, one removal won't work.
    return False

s = input()
print("YES" if can_be_made_valid_in_one_removal_or_less(s) else "NO")