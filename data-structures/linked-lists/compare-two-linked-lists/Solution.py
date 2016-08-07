"""
Author: Jordan Brown
Date: 8-6-16

Compares two linked lists to determine if they are equal.

Link to problem: https://www.hackerrank.com/challenges/compare-two-linked-lists
"""
def CompareLists(headA, headB):
    prevA = currentA = headA
    prevB = currentB = headB
    while currentA is not None and currentB is not None:
        if currentA.data != currentB.data:
            return 0
        prevA = currentA
        currentA = currentA.next
        prevB = currentB
        currentB = currentB.next
    if currentA is not None or currentB is not None:
        return 0
    return 1