"""
Author: Jordan Brown
Date: 8-13-16

Solves the sherlock and anagrams problem by counting all unordered, anagrammatic pairs
in all substrings of each input string.

Link to problem: https://www.hackerrank.com/challenges/sherlock-and-anagrams
"""
def count_anagrammatic_pairs(str):
    anagrams = {}
    for start in range(len(str)):
        for end in range(start + 1, len(str) + 1):
            anagram = "".join(sorted(str[start:end]))
            if anagram in anagrams:
                anagrams[anagram] += 1
            else:
                anagrams[anagram] = 1
    return sum((int(count*(count - 1)/2) for (str, count) in anagrams.items()))
            
for _ in range(int(input())):
    print(count_anagrammatic_pairs(input()))